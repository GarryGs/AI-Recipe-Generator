# import the necessary libraries

# import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import numpy as np
import os
from Foodimg2Ing.args import get_parser
import pickle
from Foodimg2Ing.model import get_model
from torchvision import transforms
from Foodimg2Ing.utils.output_utils import prepare_output
from PIL import Image
import time
# from tensorflow.keras.preprocessing import image
from Foodimg2Ing import app

def normalize_recipe_text(recipe_steps):

    replacements = {
        "skillet": "pan",
        "ketchup": "tomato sauce",
        "worcestershire sauce": "sauce",
        "scallions": "spring onion",
        "cilantro": "coriander",
        "ground beef": "minced meat",
        "broil": "grill",
        "saute": "lightly fry",
        "simmer": "cook",
        "olive oil": "oil",
        "medium heat": "medium flame",
        "kosher salt": "salt",
        "buns": "bread buns"
    }

    cleaned_steps = []

    for step in recipe_steps:

        step = step.lower()

        for old, new in replacements.items():
            step = step.replace(old, new)

        cleaned_steps.append(step.capitalize())

    return cleaned_steps


def clean_ingredients(ingredients):

    replacements = {
        "worcestershire_sauce": "sauce",
        "scallions": "spring onion",
        "cilantro": "coriander",
    }

    cleaned = []

    for item in ingredients:

        item = item.lower()

        if item in replacements:
            item = replacements[item]

        item = item.replace("_", " ")

        cleaned.append(item)

    return cleaned


def output(uploadedfile):

    # Keep all the codes and pre-trained weights in data directory
    data_dir=os.path.join(app.root_path,'data')


    # code will run in gpu if available and if the flag is set to True, else it will run on cpu
    use_gpu = True
    device = torch.device('cuda' if torch.cuda.is_available() and use_gpu else 'cpu')
    map_loc = None if torch.cuda.is_available() and use_gpu else 'cpu'



    # code below was used to save vocab files so that they can be loaded without Vocabulary class
    ingrs_vocab = pickle.load(open(os.path.join(data_dir, 'ingr_vocab.pkl'), 'rb'))
    vocab = pickle.load(open(os.path.join(data_dir, 'instr_vocab.pkl'), 'rb'))

    ingr_vocab_size = len(ingrs_vocab)
    instrs_vocab_size = len(vocab)
    output_dim = instrs_vocab_size

    

    t = time.time()
    import sys; sys.argv=['']; del sys
    args = get_parser()
    args.maxseqlen = 15
    args.ingrs_only=False
    model=get_model(args, ingr_vocab_size, instrs_vocab_size)
   
    # Load the pre-trained model parameters
    model_path = os.path.join(data_dir, 'modelbest.ckpt')
    model.load_state_dict(torch.load(model_path, map_location=map_loc))
    model.to(device)
    model.eval()
    model.ingrs_only = False
    model.recipe_only = False
   


    transf_list_batch = []
    transf_list_batch.append(transforms.ToTensor())
    transf_list_batch.append(transforms.Normalize((0.485, 0.456, 0.406), 
                                                (0.229, 0.224, 0.225)))
    to_input_transf = transforms.Compose(transf_list_batch)

    greedy = [True, False]
    beam = [-1, -1]
    temperature = 1.0
    numgens = len(greedy)

    uploaded_file=uploadedfile

    img = Image.open(uploaded_file).convert("RGB")    
    show_anyways = False #if True, it will show the recipe even if it's not valid
    transf_list = []
    transf_list.append(transforms.Resize(256))
    transf_list.append(transforms.CenterCrop(224))
    transform = transforms.Compose(transf_list)
    
    image_transf = transform(img)
    image_tensor = to_input_transf(image_transf).unsqueeze(0).to(device)

    num_valid = 1
    title=[]
    ingredients=[]
    recipe=[]
    for i in range(numgens):
        with torch.no_grad():
            outputs = model.sample(image_tensor, greedy=greedy[i], 
                                temperature=temperature, beam=beam[i], true_ingrs=None)
                
        ingr_ids = outputs['ingr_ids'].cpu().numpy()
        recipe_ids = outputs['recipe_ids'].cpu().numpy()
                
        outs, valid = prepare_output(recipe_ids[0], ingr_ids[0], ingrs_vocab, vocab)
            
        if valid['is_valid'] or show_anyways:
                
            title.append(outs['title'])

            cleaned_ingredients = clean_ingredients(outs['ingrs'])
            ingredients.append(cleaned_ingredients)

            cleaned_recipe = normalize_recipe_text(outs['recipe'])
            recipe.append(cleaned_recipe)
            

        else:
            title.append("Not a valid recipe!")
            recipe.append("Reason: "+valid['reason'])
            
    return title,ingredients,recipe

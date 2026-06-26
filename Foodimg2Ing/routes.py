from flask import (
    render_template,
    request,
    session,
    jsonify
)
from Foodimg2Ing import app
from Foodimg2Ing.output import output
import os
from Foodimg2Ing.chatbot import ask_recipe_question
from Foodimg2Ing.nutrition import analyze_nutrition
from Foodimg2Ing.recipe_search import generate_recipe

@app.route("/ask", methods=["POST"])
def ask():

    question = request.form["question"]

    recipe_title = session.get("recipe_title")
    recipe_text = session.get("recipe_text")
    ingredients = session.get("ingredients")

    answer = ask_recipe_question(
        recipe_title,
        recipe_text,
        ingredients,
        question
    )

    return jsonify({
        "answer": answer,
        "recipe": recipe_text,
        "ingredients": str(ingredients)
    })

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/',methods=['POST','GET'])
def predict():
    imagefile=request.files['imagefile']
    image_path=os.path.join(app.root_path,'static/images/demo_imgs',imagefile.filename)
    imagefile.save(image_path)
    img="/images/demo_imgs/"+imagefile.filename
    title, ingredients, recipe = output(image_path)

    nutrition1 = analyze_nutrition(
        title[0],
        ingredients[0],
        recipe[0]
    )

    nutrition2 = analyze_nutrition(
        title[1],
        ingredients[1],
        recipe[1]
    )

    session["recipe_text"] = "\n".join(recipe[0])
    session["ingredients"] = ", ".join(ingredients[0])

    return render_template(
        'predict.html',
        title=title,
        ingredients=ingredients,
        recipe=recipe,
        nutrition1=nutrition1,
        nutrition2=nutrition2,
        img=img
    )

@app.route('/sample/<samplefoodname>')
def predictsample(samplefoodname):

    allowed = ["sandwich", "pasta", "biryani"]

    if samplefoodname not in allowed:
        abort(404)
    
    imagefile=os.path.join(app.root_path,'static/images',str(samplefoodname)+".jpg")
    img="/images/"+str(samplefoodname)+".jpg"
    title, ingredients, recipe = output(imagefile)

    nutrition1 = analyze_nutrition(
        title[0],
        ingredients[0],
        recipe[0]
    )

    nutrition2 = analyze_nutrition(
        title[1],
        ingredients[1],
        recipe[1]
    )

    session["recipe_text"] = "\n".join(recipe[0])
    session["ingredients"] = ", ".join(ingredients[0])

    return render_template(
        'predict.html',
        title=title,
        ingredients=ingredients,
        recipe=recipe,
        nutrition1=nutrition1,
        nutrition2=nutrition2,
        img=img
    )

@app.route("/search", methods=["POST"])
def search_recipe():

    dish = request.form["dish"]

    data = generate_recipe(dish)

    titles = [
        data["recipes"][0]["title"],
        data["recipes"][1]["title"]
    ]

    ingredients = [
        data["recipes"][0]["ingredients"],
        data["recipes"][1]["ingredients"]
    ]

    recipe = [
        data["recipes"][0]["steps"],
        data["recipes"][1]["steps"]
    ]

    nutrition1 = analyze_nutrition(
        titles[0],
        ingredients[0],
        recipe[0]
    )

    nutrition2 = analyze_nutrition(
        titles[1],
        ingredients[1],
        recipe[1]
    )

    session["recipe_title"] = titles[0]
    session["recipe_text"] = "\n".join(recipe[0])
    session["ingredients"] = ", ".join(ingredients[0])

    return render_template(
        "predict.html",
        title=titles,
        ingredients=ingredients,
        recipe=recipe,
        nutrition1=nutrition1,
        nutrition2=nutrition2
    )
import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")


def ask_recipe_question(recipe_title, recipe_text, ingredients, question):

    prompt = f"""
        You are an expert cooking assistant.

        Recipe Name:
        {recipe_title}
        
        Recipe:
        {recipe_text}

        Ingredients:
        {ingredients}

        User Question:
        {question}

        Instructions:
        - Use the recipe as context and Give practical cooking advice.
        - Use your cooking knowledge to help the user.
        - If the user asks about adding an ingredient, explain how to add it and how it affects the dish.
        - If the user asks about substitutions, additions, removals, dietary changes, cooking techniques, or improvements, provide practical suggestions.
        - Do not simply state whether an ingredient appears in the recipe.
        - Explain how the ingredient can be used and how it may affect taste, texture, or cooking time.
        - Keep answers concise but helpful. Never answer with only "yes" or "no".
        """

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-3.1-flash-lite:generateContent?key={API_KEY}"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 200
        }
    }

    response = requests.post(url, json=payload)

    data = response.json()

    if "error" in data:
        return f"Gemini API Error: {data['error']['message']}"

    return data["candidates"][0]["content"]["parts"][0]["text"]
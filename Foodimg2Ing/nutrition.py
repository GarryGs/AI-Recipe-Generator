import os
import requests
import json

API_KEY = os.getenv("GEMINI_API_KEY")

def analyze_nutrition(title, ingredients, recipe):

    prompt = f"""
    You are a professional nutritionist and dietitian.

    Food Name:
    {title}

    Ingredients:
    {ingredients}

    Recipe:
    {recipe}

    Estimate realistic ingredient quantities required for ONE serving of this recipe.

    Analyze the nutrition for ONE serving only.

    Return ONLY valid JSON.

    DO NOT add explanations.
    DO NOT add markdown.
    DO NOT wrap the response in ```json.

    Required JSON format:

    {{
    "serving_size": "",
    "ingredients": [
        {{
        "name": "",
        "quantity": ""
        }}
    ],
    "calories": 0,
    "protein": 0,
    "carbs": 0,
    "fat": 0,
    "fiber": 0,
    "sugar": 0,
    "health_score": 0,
    "healthy": "",
    "reason": "",
    "healthier_version": [
        "",
        "",
        ""
    ]
    }}

    Rules:

    - calories must be in kcal
    - protein, carbs, fat, fiber and sugar must be in grams
    - health_score must be from 1 to 10
    - healthy must be one of:
    "Healthy"
    "Moderately Healthy"
    "Unhealthy"
    - healthier_version must contain exactly 3 practical suggestions
    - ingredient quantities must be realistic for one serving
    - return numeric values without units

    Example:

    {{
    "serving_size": "1 sandwich",
    "ingredients": [
        {{
        "name": "Egg",
        "quantity": "2 large"
        }},
        {{
        "name": "Bread",
        "quantity": "2 slices"
        }},
        {{
        "name": "Cheese",
        "quantity": "20"
        }}
    ],
    "calories": 420,
    "protein": 21,
    "carbs": 30,
    "fat": 22,
    "fiber": 3,
    "sugar": 2,
    "health_score": 7,
    "healthy": "Moderately Healthy",
    "reason": "Good protein content but contains moderate saturated fat and refined carbohydrates.",
    "healthier_version": [
        "Use whole wheat bread",
        "Reduce cheese quantity",
        "Add vegetables such as spinach and tomato"
    ]
    }}
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
        ]
    }

    response = requests.post(url, json=payload)
    data = response.json()

    if "error" in data:
        return data["error"]["message"]

    text = data["candidates"][0]["content"]["parts"][0]["text"]

    # Gemini often wraps JSON in ```json ... ```
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)
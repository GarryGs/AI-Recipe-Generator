import os
import json
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

def generate_recipe(dish):
    prompt = f"""
        You are an expert chef.

        Generate TWO different recipes for

        {dish}

        Return ONLY valid JSON.

        {{
        "recipes":[
            {{
            "title":"",
            "ingredients":[],
            "steps":[]
            }},
            {{
            "title":"",
            "ingredients":[],
            "steps":[]
            }}
        ]
        }}
        """

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-2.5-flash:generateContent?key={API_KEY}"
    )

    payload = {
        "contents":[
            {
                "parts":[
                    {
                        "text":prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)

    text = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    data = json.loads(text)

    return data
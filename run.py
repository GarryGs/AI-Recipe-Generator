from Foodimg2Ing import app
import os

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🍲 AI Recipe Generator")
    print("🌐 Open: http://localhost:5050")
    print("=" * 60 + "\n", flush=True)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )
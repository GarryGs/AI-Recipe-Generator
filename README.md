AI Recipe Generator 🍛

Transform food images into complete cooking recipes using Deep Learning, Computer Vision, and Natural Language Generation.

Upload a food image and the model will generate:

* 🍽 Recipe Title
* 🥕 Ingredient List
* 👨‍🍳 Cooking Instructions

The project is built using:

* Flask
* PyTorch
* Torchvision
* HTML/CSS/Bootstrap

⸻

Features

* Food image upload support
* AI-based ingredient prediction
* AI-generated recipe instructions
* Multiple recipe outputs
* Indian-friendly recipe wording customization
* Docker support for cross-platform setup
* Responsive UI

⸻

Project Structure

AI-Recipe-Generator/
│
├── Foodimg2Ing/
│   ├── data/
│   │   ├── modelbest.ckpt
│   │   ├── ingr_vocab.pkl
│   │   └── instr_vocab.pkl
│   ├── Templates/
│   ├── static/
│   ├── model.py
│   ├── output.py
│   └── routes.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md

⸻

Requirements

* Docker
* Docker Compose

OR

* Python 3.8.18
* pip

⸻

Run Using Docker (Recommended) 🐳

This is the easiest and most reliable setup.

1. Clone Repository

git clone https://github.com/GarryGs/AI-Recipe-Generator.git
cd AI-Recipe-Generator

⸻

2. Start Application

docker compose up --build

⸻

3. Open in Browser

http://localhost:5000

⸻

Run Without Docker

1. Install Python 3.8.18

Recommended using pyenv:

pyenv install 3.8.18
pyenv local 3.8.18

⸻

2. Create Virtual Environment

Linux / macOS

python -m venv venv
source venv/bin/activate

Windows

python -m venv venv
venv\Scripts\activate

⸻

3. Install Dependencies

pip install -r requirements.txt

⸻

4. Run Application

python run.py

⸻

5. Open in Browser

http://localhost:5000

⸻

Model Files

The pretrained model and vocabulary files are already included inside:

Foodimg2Ing/data/

Files:

* modelbest.ckpt
* ingr_vocab.pkl
* instr_vocab.pkl

⸻

Sample Predictions

Input:

Food image uploaded by user

Output:

* Recipe title
* Ingredients
* Cooking steps

⸻

Tech Stack

Component	Technology
Backend	Flask
ML Framework	PyTorch
Frontend	HTML/CSS/Bootstrap
Image Processing	Pillow
Deployment	Docker

⸻

Notes

* First startup may take some time because the AI model loads into memory.
* Docker setup is recommended for best compatibility across Linux, macOS, and Windows.
* The project uses CPU inference by default.

⸻

Future Improvements

* Faster inference
* Better Indian cuisine support
* Modern frontend redesign
* API support
* Mobile responsive UI improvements
* Cloud deployment

⸻

License

This project is intended for educational and research purposes.

⸻

Author

Developed and customized by GarryGs.
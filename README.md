# AI Recipe Generator 🍛

Transform food images into complete cooking recipes using Deep Learning, Computer Vision, and Natural Language Generation.

Upload a food image and the model will generate:

- 🍽 Recipe Title
- 🥕 Ingredient List
- 👨‍🍳 Cooking Instructions

The project is built using:

- Flask
- PyTorch
- Torchvision
- HTML/CSS/Bootstrap

---

# ✨ Features

- Food image upload support
- AI-based ingredient prediction
- AI-generated recipe instructions
- Multiple recipe outputs
- Indian-friendly recipe wording customization
- Docker support for cross-platform setup
- Responsive UI

---

# 📁 Project Structure

```bash
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
```

---

# ⚙️ Requirements

You can run the project using either:

## Option 1 — Docker (Recommended)

- Docker
- Docker Compose

OR

## Option 2 — Local Python Setup

- Python 3.8.18
- pip

---

# 🐳 Run Using Docker (Recommended)

This is the easiest and most reliable setup.

## 1. Clone Repository

```bash
git clone https://github.com/GarryGs/AI-Recipe-Generator.git
cd AI-Recipe-Generator
```

---

## 2. Start Application

```bash
docker compose up --build
```

---

## 3. Open in Browser

```text
http://localhost:5000
```

---

# 💻 Run Without Docker

## 1. Install Python 3.8.18

Recommended using pyenv:

```bash
pyenv install 3.8.18
pyenv local 3.8.18
```

---

## 2. Create Virtual Environment

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python run.py
```

---

## 5. Open in Browser

```text
http://localhost:5000
```

---

# 🧠 Model Files

The pretrained model and vocabulary files are already included inside:

```bash
Foodimg2Ing/data/
```

Files included:

- `modelbest.ckpt`
- `ingr_vocab.pkl`
- `instr_vocab.pkl`

---

# 📸 Sample Output

### Input

Food image uploaded by user

### Output

- Recipe title
- Ingredients list
- Cooking instructions

---

# 🛠 Tech Stack

| Component | Technology |
|---|---|
| Backend | Flask |
| ML Framework | PyTorch |
| Frontend | HTML/CSS/Bootstrap |
| Image Processing | Pillow |
| Deployment | Docker |

---

# 📝 Notes

- First startup may take some time because the AI model loads into memory.
- Docker setup is recommended for best compatibility across Linux, macOS, and Windows.
- The project uses CPU inference by default.

---

# 🚀 Future Improvements

- Faster inference
- Better Indian cuisine support
- Modern frontend redesign
- API support
- Mobile responsive UI improvements
- Cloud deployment

---

# 📄 License

This project is intended for educational and research purposes.

---

# 👨‍💻 Author

Developed and customized by **GarryGs**
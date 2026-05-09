# AI Recipe Generator 🍽️

An AI-powered web application that generates cooking recipes from food images using Deep Learning, Computer Vision, and Natural Language Processing.

Upload a food image and the system will automatically:

* identify likely ingredients
* generate recipe titles
* create cooking instructions
* produce human-friendly recipe outputs

The project is built using Flask, PyTorch, CNNs, and Transformer-based sequence generation models.

---

## Features

* 📸 Food Image Upload
* 🤖 AI-Based Recipe Generation
* 🧂 Ingredient Prediction
* 👨‍🍳 Step-by-Step Cooking Instructions
* 🌍 Natural Cooking Language Enhancement
* 🎨 Modern Web Interface
* 🧠 Deep Learning + Transformer Architecture

---

## Tech Stack

### Backend

* Python
* Flask
* PyTorch
* TensorFlow/Keras

### AI / Deep Learning

* CNN Image Encoder
* Transformer Decoder
* Attention Mechanism
* NLP-based Recipe Generation

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

---

## Project Structure

```bash
Foodimg2Ing/
│
├── model.py                # Main AI model pipeline
├── routes.py               # Flask routes
├── output.py               # Recipe generation and formatting
├── modules/                # Transformer & encoder modules
├── Templates/              # HTML templates
├── static/                 # CSS, JS, images
└── data/                   # Trained model + vocab files
```

---

## Model Files

This project uses pretrained model weights and vocabulary files stored inside:

```bash
Foodimg2Ing/data/
```

Required files:

* `modelbest.ckpt`
* `ingr_vocab.pkl`
* `instr_vocab.pkl`

---

## Requirements

* Python 3.8.18
* Git LFS (required for large model files)

---

## Setup Instructions

### 1. Install Git LFS

```bash
git lfs install
```

### 2. Clone Repository

```bash
git clone https://github.com/GarryGs/AI-Recipe-Generator.git"
cd "AI-Recipe-Generator"
```

### 3. Install Python 3.8

Using pyenv:

```bash
pyenv install 3.8.18
pyenv local 3.8.18
```

### 4. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Application

```bash
python run.py
```

Open the localhost URL shown in the terminal inside your browser.

---

## Future Improvements

* Better cuisine detection
* Recipe regeneration modes
* Nutrition estimation
* Save recipe history
* Mobile responsiveness
* Improved recipe formatting
* Enhanced Indian and global cuisine support

---

## Disclaimer

The generated recipes are AI-generated predictions and may not always perfectly match the uploaded food image.

---

## License

This project is intended for educational and learning purposes.

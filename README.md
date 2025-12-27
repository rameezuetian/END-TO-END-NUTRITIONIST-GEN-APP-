# 🥗 End-to-End Nutritionist Generative AI App

An **End-to-End AI-powered Nutritionist Application** built using **Streamlit** and **Google Gemini API**. This app allows users to upload food images and receive an AI-generated analysis including estimated calories, nutrients, and health impact.

---

## 🚀 Features

* 📸 Upload food images (JPG, JPEG, PNG)
* 🧠 AI-powered food analysis using **Google Gemini**
* 🔥 Estimated calorie count
* 🥦 Nutritional breakdown
* ❤️ Health impact insights
* 🌐 Simple and interactive Streamlit UI

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** – Frontend/UI
* **Google Gemini API** – Multimodal Generative AI
* **Pillow (PIL)** – Image processing
* **python-dotenv** – Environment variable management

---

## 📂 Project Structure

```
END-TO-END-NUTRITIONIST-GEN-APP
│
├── app.py              # Main Streamlit application
├── .env                # Environment variables (API Key)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## 🔑 Environment Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/rameezuetian/END-TO-END-NUTRITIONIST-GEN-APP-.git
cd END-TO-END-NUTRITIONIST-GEN-APP-
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup `.env` file

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> 🔔 Get your API key from **Google AI Studio**

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 📸 How It Works

1. Upload an image of food
2. Click **"Tell me about total calories"**
3. Gemini AI analyzes the image
4. Receive calories, nutrients & health insights

---

## ⚠️ Notes

* This project uses the **new Gemini API (`google-genai`)**
* Older Gemini models and SDKs are deprecated
* Ensure your API key has **Gemini access enabled**

---

## 📌 Future Improvements

* 🍱 Meal-wise calorie tracking
* 📄 PDF & document support
* 🧮 BMI & daily calorie calculator
* ☁️ Cloud deployment (Streamlit Cloud / Docker)

---

## 👨‍💻 Author

**Muhammad Rameez**
Computer Science Student | AI / ML Enthusiast
University of Engineering & Technology, Lahore

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

Happy Coding 🚀

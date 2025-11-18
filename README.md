# World Economic Indicator – GDP Prediction Project

This project is part of the **ML Zoomcamp Midterm** and focuses on predicting **GDP** using global economic indicators such as inflation, unemployment, population, interest rates, and more.

The project includes:

* Exploratory data analysis
* Feature engineering
* Multiple regression models
* Model selection
* Saving the best model
* Deploying a prediction service using **Flask**
* Containerization with **Docker**

---

## 🧠 1. Project Overview

This project uses a dataset from the **World Bank** (CSV format) to build a machine learning model that predicts **GDP** for each country and year.

The workflow includes:

1. Data cleaning & preprocessing
2. Exploratory data analysis
3. Training baseline & advanced ML models
4. Evaluating MAE, RMSE, R²
5. Saving the final model with `pickle`
6. Building a web API using Flask (`/predict` endpoint)
7. Creating a Docker container for deployment
8. Publishing everything to GitHub

---

This is my submission for the **ML Zoomcamp Midterm Project**.

---

## 📁 Project Files

```
World-Economic-Indicator/
│
├── app/
│   └── main.py            # Flask web service
│
├── models/
│   └── main.py            # Model training script
│
├── notebooks/
│   └── World Economic Indicator.ipynb  # Main notebook
│
├── model.pkl              # Saved machine learning model
├── requirements.txt       # Python packages
├── Dockerfile             # For running with Docker
└── README.md
```

---

## 📊 What the Project Does

1. Loads a dataset of world economic indicators
2. Cleans the data
3. Trains ML models to predict GDP
4. Saves the best model
5. Runs a simple API where you can send numbers and get a GDP prediction

---

## 🚀 How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the web service

```bash
python app/main.py
```

The API will start at:

```
http://localhost:8000
```

---

## 🔮 Example Prediction Request

Send a POST request to:

```
http://localhost:8000/predict
```

Example JSON:

```json
{
  "inflation": 2.5,
  "unemployment": 5.1,
  "population": 45000000,
  "interest_rate": 1.2
}
```

---

## 🐳 Running with Docker

Build the image:

```bash
docker build -t gdp-service .
```

Run it:

```bash
docker run -p 8000:8000 gdp-service
```

---

## 📝 Notes

* This project is for learning and practicing machine learning deployment
* The model used is simple and not optimized
* The goal is to show the full process from training → saving → deployment

---

## 👩‍💻 Author
Developed by **Christina Ravichandran**
For ML Zoomcamp Midterm Submission.

---

If you'd like, I can also:

✔ Format this automatically in GitHub style
✔ Add badges (Python version, Docker ready, etc.)
✔ Add screenshots of your notebook or API testing

Just let me know!

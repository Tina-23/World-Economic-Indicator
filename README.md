# World-Economic-Indicator — ML Regression Project

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

## 📁 2. Repository Structure

```bash
World-Economic-Indicator/
│
├── app/
│   ├── main.py             # Flask API
│   └── model.pkl           # saved ML model
│
├── models/
│   └── main.py             # ML training script
│
├── notebooks/
│   └── World Economic Indicator, Mid term project - fixed.ipynb
│
├── requirements.txt        # project dependencies
├── Dockerfile              # container setup
├── pyproject.toml          # poetry config (optional)
├── .gitignore
└── README.md
```

---

## 🧪 3. Model Training

All ML work is done in:

```
models/main.py
```

This script:

* Loads the dataset
* Splits into train/test
* Builds preprocessing pipelines
* Trains Linear Regression & Random Forest
* Selects the best model
* Saves it as `model.pkl`

---

## 🔮 4. API Usage (Flask Web Service)

Run the service:

```bash
python app/main.py
```

The API exposes one endpoint:

### **POST /predict**

Example request:

```json
{
  "inflation": 2.5,
  "unemployment": 6.2,
  "population": 50000000,
  "interest_rate": 1.8
}
```

Example response:

```json
{
  "gdp_prediction": 43829.42
}
```

---

## 🐳 5. Running with Docker

Build the Docker image:

```bash
docker build -t gdp-service .
```

Run the container:

```bash
docker run -p 8000:8000 gdp-service
```

API will be available at:

```
http://localhost:8000/predict
```

---

## 🌐 6. Optional: Deploy to Cloud

You may deploy to:

* AWS EC2
* Render
* Railway
* Fly.io

The Dockerfile supports cloud deployment with no modification.

---

## 📦 7. Installation (Local)

Create environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📝 8. Requirements

* Python 3.10
* Scikit-Learn
* Pandas
* NumPy
* Flask
* Docker (for containerized deployment)

---

## 📬 9. Contact

Developed by **Christina Ravichandran**
For ML Zoomcamp Midterm Submission.

---

If you'd like, I can also:

✔ Format this automatically in GitHub style
✔ Add badges (Python version, Docker ready, etc.)
✔ Add screenshots of your notebook or API testing

Just let me know!

# 🌸 Iris Flower Classification – Machine Learning Project

## 📌 Project Overview

This project implements a Machine Learning model to classify iris flowers into three different species based on their physical measurements. The classification is performed using supervised learning algorithms from the Scikit-learn library.

The project demonstrates a complete machine learning workflow including data loading, preprocessing, model training, evaluation, and prediction.

---

## 📊 Dataset Information

The Iris dataset contains 150 samples with the following features:

* Sepal Length (cm)
* Sepal Width (cm)
* Petal Length (cm)
* Petal Width (cm)

### Target Classes

* Setosa
* Versicolor
* Virginica

---

## 🧠 Machine Learning Workflow

The project follows the standard ML pipeline:

1. Data Loading
2. Data Preprocessing
3. Train-Test Split
4. Model Training
5. Model Evaluation
6. Model Saving
7. Prediction

---

## 🤖 Model Used

* Logistic Regression (Primary Model)
* Future scope: KNN, Decision Tree, SVM

---

## 📁 Project Structure

```
iris-ml-project/
│
├── data/
│   └── iris.csv
│
├── models/
│   └── iris_model.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   └── preprocess.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yashrajbhawgat7-create/iris_ml_prediction.git
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

Run the main file:

```
python main.py
```

This will:

* Train the model
* Evaluate the model
* Save the trained model
* Run a sample prediction

---

## 📈 Model Evaluation

The model is evaluated using:

* Accuracy Score
* Confusion Matrix
* Train-Test Split Validation

---

## 🔮 Future Improvements

* Add multiple ML models and compare performance
* Hyperparameter tuning
* Add Streamlit web application
* Deploy the model
* Add data visualization dashboard
* Convert project into REST API using Flask

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Seaborn
* Joblib

---

## 📚 Learning Outcomes

From this project, the following concepts are demonstrated:

* Machine Learning pipeline
* Data preprocessing
* Model training and evaluation
* Model serialization
* Project structuring for production-like environment

---

## 👨‍💻 Author

Yashraj Kailas Bhagwat
Engineering Student – Machine Learning Project

---

## 📄 License

This project is for educational and learning purposes.

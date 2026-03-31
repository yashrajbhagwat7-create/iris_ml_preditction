from sklearn.metrics import classification_report, confusion_matrix
import joblib
import pandas as pd
data_path = 'data/Iris.csv'
model_path = 'models/model.pkl'
def evaluate_model(data_path, model_path):
    # Load dataset
    data = pd.read_csv(data_path)

    # Split features and target
    X = data.drop(['Id', 'Species'], axis=1)
    y = data['Species']

    # Load the trained model
    model = joblib.load(model_path)

    # Make predictions
    y_pred = model.predict(X)

    # Evaluate the model
    print("Classification Report:")
    print(classification_report(y, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y, y_pred))
evaluate_model(data_path, model_path)    
import joblib
import numpy as np

# Load model
model = joblib.load("models/model.pkl")

# Example flower
sample = np.array([[5.1, 3.5, 1.4, 0.2]])

prediction=model.predict(sample)
print("Predicted class:", prediction)
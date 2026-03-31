import os

print("Training model...")
os.system("python src/train.py")

print("Evaluating model...")
os.system("python src/evaluate.py")

print("Running prediction...")
os.system("python src/predict.py")
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
data_path='data/Iris.csv'
model_path='models/model.pkl'
def train_model(data_path,model_path):
    #load dataset
    data=pd.read_csv(data_path)

    #split features and target
    X=data.drop(['Id', 'Species'],axis=1)
    y=data['Species']

    #split data into training and testing sets
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    #initialize and train the model
    model=LogisticRegression()
    model.fit(X_train,y_train)

    #save the trained model
    joblib.dump(model,model_path)
    print(f'Model trained and saved to {model_path}')

train_model(data_path, model_path)

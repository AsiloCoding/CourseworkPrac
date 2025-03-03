import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

class LogReg():
    def __init__(self):
        self.df = pd.read_csv("CourseworkDF.csv", header = 0)
        self.features = ["FTr","eFG%", "TOV%", "ORB%"]
        X = self.df[self.features]
        self.df["WinR"] = (self.df["WinR"] >= 0.5).astype(int)
        y = self.df["WinR"]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.25, random_state = 8)
    
    def ModelTraining(self, data):
        scaler = StandardScaler()
        self.X_train_scaled = scaler.fit_transform(self.X_train)
        self.X_test_scaled = scaler.transform(self.X_test)
        data = self.df[(self.df["Team"] == data) & (self.df["Season"] == "2024-25")]
        data = data[self.features]
        self.input = scaler.transform(data)
        self.logreg = LogisticRegression(random_state = 8, max_iter = 500)
        self.logreg.fit(self.X_train_scaled, self.y_train)
    
    def Prediction(self):
        self.y_pred = self.logreg.predict(self.X_test_scaled)
        self.y_prob = self.logreg.predict_proba(self.input)
        return self.y_prob[0][1]

Team = "New Orleans Pelicans"
RegressionModel = LogReg()
RegressionModel.ModelTraining(Team)
probability = RegressionModel.Prediction()
print(f"{probability:.1%}")
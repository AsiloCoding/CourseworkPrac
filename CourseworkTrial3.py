import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Reading csv file
col_names = ["pregnant", "glucose", "bp", "skin", "insulin", "bmi", "pedigree", "age", "label"]
df = pd.read_csv("diabetes.csv", header=0, names=col_names)

# Feature selection
features = ["pregnant", "glucose", "bp", "skin", "insulin", "bmi", "pedigree", "age"]
X = df[features]
y = df.label

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training the model
logreg = LogisticRegression(random_state=16, max_iter=500)
logreg.fit(X_train_scaled, y_train)

# Making predictions
y_pred = logreg.predict(X_test_scaled)



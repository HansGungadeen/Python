import numpy as np
import matplotlib
import pandas as pd

path = "iris.data"

headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = pd.read_csv(path, names=headernames)
dataset.head()

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.40)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=8)
classifier.fit(X_train, Y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

result = confusion_matrix(Y_test,y_pred)
print("Confusion Matrix: ")
print(result)

result1 = classification_report(Y_test,y_pred)
print("Classification Report: ")
print(result1)

result2 = accuracy_score(Y_test,y_pred)
print("Accuracy: ", result2)
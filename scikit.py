import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('iris.csv')

X = df[['SepalLengthCm', 'SepalWidthCm',
    'PetalLengthCm', 'PetalWidthCm']]
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(  X, y, test_size=0.2, random_state=77
)
clf = RandomForestClassifier(random_state=77)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print(pred)

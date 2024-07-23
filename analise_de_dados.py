from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC

import pandas as pd

train = pd.read_excel("Treinamento.xlsx")
test = pd.read_excel("Teste.xlsx")
x = train["Tweet"]
tfidf = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
X = tfidf.fit_transform(x)
y = train["Label"]
X.shape
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
x_train.shape, x_test.shape

clf = LinearSVC()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

print(classification_report(y_test, y_pred))

print("A taxa de acurácia do ML e de " + str(accuracy_score(y_test, y_pred)*100) + "%")
score = []
for tweet in test["Tweet"]:
    vec = tfidf.transform([str(tweet)])
    score.append(int(clf.predict(vec)))

from collections import Counter
positive = Counter(score)[0]/(Counter(score)[0] + Counter(score)[1]) * 100
negative = (positive - 100) * -1

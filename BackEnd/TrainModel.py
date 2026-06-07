import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

dados = pd.read_csv("dataset/spam.csv")

X = dados["mensagem"]
y = dados["classe"]

vectorizer = TfidfVectorizer()

X_tfidf = vectorizer.fit_transform(X)

modelo = MultinomialNB()
modelo.fit(X_tfidf, y)

pickle.dump(modelo, open("model/spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("Modelo treinado com sucesso!")

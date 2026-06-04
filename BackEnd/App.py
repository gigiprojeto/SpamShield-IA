from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import sqlite3

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    mensagem = data["mensagem"]

    texto = vectorizer.transform([mensagem])
    resultado = model.predict(texto)[0]

    conn = sqlite3.connect("database/spamshield.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO historico (mensagem, resultado) VALUES (?, ?)",
        (mensagem, resultado)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "resultado": resultado
    })

if __name__ == "__main__":
    app.run(debug=True)

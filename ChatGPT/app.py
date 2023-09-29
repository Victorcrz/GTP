from flask import Flask, render_template, request
import openai
import re

app = Flask(__name__)
historialchat = []


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pregunta = request.form.get("pregunta")
        resultado = enviar_pregunta(pregunta)
        oraciones = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', resultado)
        historialchat.append({"YO": pregunta})
        for oracion in oraciones:
            historialchat.append({"ChatGPT": oracion})
    else:
        chat = ""
    return render_template("index.html", historial=historialchat)


def enviar_pregunta(pregunta):
    openai.api_key = "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"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": pregunta
            }
        ]
    )
    return respuesta["choices"][0]["message"]["content"]


if __name__ == '__main__':
    app.run(debug=True, port=5000)

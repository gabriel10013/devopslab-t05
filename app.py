from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    today = date.today()
    return "Good morning, today is "+today


if __name__ == '__main__':
    app.run()
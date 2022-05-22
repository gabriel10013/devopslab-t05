from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    today = "Good Morning, today is" date.today()
    return today

if __name__ == '__main__':
    app.run()
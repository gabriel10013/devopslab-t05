from flask import Flask
from flask_wtf.csrf import CSRFProtect
from datetime import date

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    today = "Good Morning, today is " + str(date.today())
    return today
 
if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)
from flask import Flask, render_template

app = Flask(__name__)

# Rota principal
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


# Exemplo de rota para página de cadastro (se criar cadastro.html)
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


if __name__ == "__main__":
    app.run(debug=True)
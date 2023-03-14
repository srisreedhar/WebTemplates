from flask import Flask
app = Flask(__name__)



@app.route("/")
def hello():
    return " Hellow Cats "

@app.route("/products")
def indexpage():
    return " This is ProductsPage "

@app.route("/contactus")
def contactus():
    return " please constact us  "


@app.route("/aboutus")
def aboutus():
    return " About us  "


if __name__ == "__main__":
    app.run()
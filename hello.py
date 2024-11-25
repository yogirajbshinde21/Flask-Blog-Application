from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)


# Create a route decorator
# @app.route('/')
# def index():
#     return "<h1>Hello, Worldd!</h1>"

@app.route('/')
def index():
    first_name = "Yogiraj"
    stuff = "This is <strong> Bold </strong> stuff"
    thing = "This is another thing"
    dishes = ["Biryani", "Chicken", "Fish",44]
    return render_template("index.html", first_name=first_name, stuff=stuff, thing=thing, dishes=dishes)

# localhost:5000/user/Yogiraj
# @app.route('/user/<name>')
# def user(name):
#     return f"How are you {name} ?"

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)


# Create customer Error Pages

# Invalid URL:
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

# Internal Server Error:
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500











if __name__=="__main__":
    app.run(debug=True)
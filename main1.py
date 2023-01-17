"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template





# Create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("index.html")


# Create a URL route in our application for "/people"
@connex_app.route("/comments")
@connex_app.route("/comments")
def people(person_id=""):
    """
    This function just responds to the browser URL
    localhost:5000/people

    :return:        the rendered template "people.html"
    """
    return render_template("index1.html")

if __name__ == "__main__":
    app.run(localhost, port= 3306, debug=True)

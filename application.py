from flask import Flask, render_template,request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show our first page which is an application form."""

    return render_template("application-form.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application", methods=['POST'])
def greeting():
    """taking the input from the form and rendering it

    rendering to the application-response.html form
    """

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    quantity = request.form.get('quantity')
    typeofjob = request.form.get('typeofjob')
   
    return render_template("application-response.html",firstname=firstname
        ,lastname=lastname,quantity=quantity,typeofjob=typeofjob)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")


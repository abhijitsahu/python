from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = "18e993f97a115028f1b97ed689a9d31e"
# List of dict
# Each dict contains single blog posts


@app.route("/")
@app.route("/home")
def Home():
    return render_template('home.html')


@app.route("/about")
def about():
    # This is h1 heading for about page
    return render_template('about.html', title='About')


# @app.route("/register")
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)

"""
This Is My First Web App
This Was Created In 6/6/2023
Basel Ashraf Created This App
"""


from flask import Flask


the_app = Flask(__name__)

@the_app.route("/")
def say_hi():
    """ This Fucntion Returns A String """
    return "Hello From Say Hi Function"

@the_app.route("/home")
def say_welcome():
    """ This Function Returns A String """
    return "Welcome To The Home Page :)"


@the_app.route("/skills")
def skills():
    """ This Function Return A String """
    return "I'm Good At Python"



if __name__ == "__main__":
    the_app.run()

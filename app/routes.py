from flask import Flask  # From the flask module import the Flask class

# OOP -> Object Oriented Paradigm

app = Flask(__name__)           # Creates an instance of the Flask class
# object


# Flask decorator that maps view functions to routes
@app.get("/aboutme")
def about_me():                 # Our view function
    me = {                      # Python dictionary
        "first_name": "Romnick",
        "last_name": "Sarmiento",
        "hobbies": "Gaming",
        "is_active": True
    }
    return me                   # return statement (returned to caller)

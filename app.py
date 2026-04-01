import os
print("Running file:", os.path.abspath(__file__))

from flask import Flask #flask is a python web framework, importing its class
from flask import render_template # this allows us to use html templates in our flask app

# Initializing web server
app = Flask(__name__) #an instance (my app) of the flask framework

@app.route("/") # when in root dir, call this function
def home():
    return render_template("home.html") # render the home.html template

if __name__== "__main__": # if currently running this file then run the server
    print("Inside the main block - Starting Flask...") # This confirms the IF statement works
    app.run(debug=True)
else:
    print("3. Failed! I am not being run as the main script.")
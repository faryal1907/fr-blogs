from flask import Flask #flask is a python web framework, importing its class

# Initializing web server
app = Flask(__name__) #an instance (my app) of the flask framework

@app.route("/") # when in root dir, call this function
def home():
    return "Welcome to my Thought-Dump!"

if __name__== "__main__": # if currently running this file then run the server
    print("Inside the main block - Starting Flask...") # This confirms the IF statement works
    app.run(debug=True)
else:
    print("3. Failed! I am not being run as the main script.")
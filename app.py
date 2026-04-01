from flask import Flask , render_template 

app = Flask(__name__) #an instance (my app) of the flask framework

@app.route("/") 
def home():

    
    
    articles = [
        {"title":"My First Blog Post", "date": "2026-04-01"},
        {"title":"I have thunken more thoughts", "date": "2026-04-01"}
    ]

    
    return render_template("home.html", articles=articles) 

if __name__== "__main__":
    app.run(debug=True)

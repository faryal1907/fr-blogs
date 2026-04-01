from flask import Flask , render_template, request, redirect
import json
import os
from datetime import datetime


app = Flask(__name__) #an instance (my app) of the flask framework

@app.route("/")
def home():
    articles = []

    for filename in os.listdir("articles"):  # list all files in the "articles" directory
        if filename.endswith(".json"):
            filepath = os.path.join("articles", filename) # create the full path to the file > articles/1.json

            with open(filepath, "r") as file:
                '''In Python, with and as are used together to create what is called a Context Manager. Think of it as a "Safety Sandwich."
                 It makes sure that no matter what happens inside the sandwich (even if there is an error), the "cleanup" happens 
                 automatically at the end.'''
                data = json.load(file)

                data["id"] = filename.replace(".json", "") # remove the .json extension from the filename to get the article ID

                articles.append(data)

    return render_template("home.html", articles=articles)


@app.route("/article/<id>")
def article(id):
    filepath = os.path.join("articles", f"{id}.json")

    with open(filepath, "r") as file:
        data = json.load(file)

    return render_template("article.html", article=data) 


@app.route("/add", methods=["GET", "POST"])
def add_article():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        date = datetime.now().strftime("%Y-%m-%d")

        # create new article
        new_article = {
            "title": title,
            "content": content,
            "date": date
        }

        # generate new ID
        files = os.listdir("articles")
        new_id = len(files) + 1

        filepath = os.path.join("articles", f"{new_id}.json")

        with open(filepath, "w") as file:
            json.dump(new_article, file)

        print(request.form)

        return redirect("/")

    return render_template("add.html")

if __name__== "__main__":
    app.run(debug=True)

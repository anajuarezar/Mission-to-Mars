from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars



# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
client = pymongo.MongoClient(conn)


@app.route("/")
def home():

    # Find one record of data from the mongo database
    news_title = list(mongo.db.collection.find)[0]
    news_par =  list(mongo.db.collection.find)[1]
    featured_im = list(mongo.db.collection.find)[2]


    # Return template and data
    return render_template("index.html", news_title=news_title, news_par=news_par, featured_im=featured_im)


@app.route("/scrape")
def scrape():

    # Run the scrape function
    data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


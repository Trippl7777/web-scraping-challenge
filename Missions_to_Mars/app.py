from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# Pass connection to the pymongo instance.




app.config["MONGO_URI"] = "mongodb://localhost:27017/web_scrape"




mongo = PyMongo(app)

@app.route("/")
def index():
    # data_collection = mongo.db.web_scrape.find_one()
    # print(data_collection)
    # return render_template("index.html", data_collection=data_collection)
    if (mongo.db.data_collection.find_one() == None):
        data_collection = mongo.db.data_collection
    else:
        data_collection = mongo.db.data_collection.find_one()
    return render_template('/index.html', data_collection=data_collection)


# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():
    data = scrape_mars.scrape()
    mongo.db.data_collection.insert_one(data)
    #data.update({}, data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

###you've successfully added one data set, now add the rest into the object (collection) but name it whatever you want
# collection.title1 = "Cerberus..." update collection table name
# once added, now you need to put in some kind of format (bootstrap CARD, simple table, row, column)
# {{collection.title}} like this > <h4 class="heading">{{listings.price}} {{listings.headline}}</h4>
# pictures you have to show w/ <img> resize probably most likely surely


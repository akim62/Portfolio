# dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# connect to mongodb
app.config["MONGO_URI"] = "mongodb://localhost27017/mars_app"
mongo = PyMongo(app)

# create routes
@app.route('/')
def index():
    mars_listings = mongo.db.mars_listings.find_one()
    return render_template("index.html", mars_listings=mars_listings)

@app.route('/scrape')
def scraper():
    mars_listings = mongo.db.mars_listings

    mars_data = scrape_mars.news_scrape()
    mars_data = scrape_mars.img_scrape()
    mars_data = scrape_mars.twitter_scrape()
    mars_data = scrape_mars.facts_scrape()
    mars_data = scrape_mars.hemi_scrape()
    mars_listings.update({}, mars_data, upsert=True)

    return redirect('/', code=302)



if __name__ == "__main__":
    app.run(debug=True)
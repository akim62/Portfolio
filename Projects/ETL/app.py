from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_glassdoor

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/tech_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    listings = mongo.db.listings.find_one()
    return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():
    listings = mongo.db.listings
    listings_glass = scrape_glassdoor.scrape_glassdoor("https://www.glassdoor.com/Job/jobs.htm?sc.keyword=full%20stack%20developer&locT=C&locId=1146798&locKeyword=Irvine,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=25&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=1&remoteWorkType=0")
    listings_indeed = scrape_glassdoor.scrape_indeed("https://www.indeed.com/jobs?q=developer&l=Irvine%2C%20CA&start=10&advn=6908518619934192&vjk=9fc0a07016cd1dbf")
    listings.update({}, listings_glass, listings_indeed, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

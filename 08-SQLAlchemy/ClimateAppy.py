# import dependencies

from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy import create_engine, func, and_, or_
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

import datetime as dt

# create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect database
Base = automap_base()
Base.prepare(engine, reflect=True)

# store tables into variables
Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask setup
app = Flask(__name__)


@app.route("/")
def home():
    return (
        f"Routes:</br>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/<start></br>"
        f"/api/v1.0/<start>/<end></br>"
          )

@app.route("/api/v1.0/precipitation")
def precipitation():

    # find precipitation for last year by getting last date in data and subtracting a year from it
    last_date = session.query(func.max(func.strftime("%Y-%m-%d", Measurement.date))).all()
    first_date = laste_date - dt.timedelta(days=365)

    # prcp data after first_date
    prcp = session.query(func.strftime("%Y-%m-%d", Measurement.date), Measurement.prcp).\
        filter(func.strftime("%Y-%m-%d", Measurement.date) >= first_date).all()

    prcp_list = []

    for data in prcp:
        prcp_dict = {}

    return jsonify(prcp_list)

@app.route("/api/v1.0/stations")
def stations():

    # create session
    session = Session(engine)
    all_stations = session.query(Stations).all()

    stations_list = []

    for station in all_stations:
        stations_dict = {}
        stations_dict['id'] = station.id
        stations_dict['station'] = station.station
        stations_dict['name'] = stations.name
        stations_dict['latitude'] = stations.latitude
        stations_dict['longitude'] = stations.longitude
        stations_dict['elevation'] = stations.elevation
        stations_list.append(stations_dict)

    return jsonify(stations_list)

    

@app.route("/api/v1.0/tobs")
def tobs():

    # find tobs for last year by getting last date in data and subtracting a year from it
    last_date = session.query(func.max(func.strftime("%Y-%m-%d", Measurement.date))).all()
    first_date = laste_date - dt.timedelta(days=365)

    # tobs data after first_date
    tobs_data = session.query(func.strftime("%Y-%m-%d", Measurement.date), Measurement.tobs).\
        filter(func.strftime("%y-%m-%d", Measurement.date) >= first_date).all()

    tobs_list = []

    for tob in tobs_data:
        tobs_dict = {}
        tobs_dict['date'] = tob.date
        tobs_dict['station'] = tob.station
        tobs_dict['tobs'] = tob.tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)
    

@app.route("/api/v1.0/<start></br>")
def start():

    # get last date in data and subtract year from it
    last_date = session.query(func.max(func.strftime("%Y-%m-%d", Measurement.date))).all()
    first_date = last_date - dt.timedelta(days=365)

    # use calc_temps function to get temperatures
    temp = calc_temps(first_date, last_date)


    

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    





if __name__ == "__main__":
    app.run(debug=True)

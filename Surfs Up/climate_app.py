{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}


import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:////Users/yaden/Desktop/sqlalchemy-challenge/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

# Create session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Home route with list of all available API routes

@app.route("/")
def home():

    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/2016-08-23</br>" 
     )

#################################################  

# Return a list of precipitation values for August 23, 2016 - 2017

@app.route("/api/v1.0/precipitation")
def percipitation():
        prcp = session.query(func.strftime("%Y-%m-%d", measurement.date), measurement.prcp).\
        filter(func.strftime("%Y-%m-%d", measurement.date) >= "2016-08-23").all()
        
        results_dict = {}
        for result in prcp:
            results_dict[result[0]] = ({"PRCP (in.)":result[1]})
        
        return jsonify(results_dict)
        
#    Return a list of all stations

@app.route("/api/v1.0/stations")
def stations():
    station_query= session.query(station.station, station.name).all()
    station_list = list(station_query)
    
    return jsonify(station_list)

#################################################  

# Query the dates and temperature observations of 
# the most active station for the last year of data

@app.route("/api/v1.0/tobs")

def tobs():
        tobs_data = session.query(func.strftime("%Y-%m-%d", measurement.date), measurement.station, measurement.tobs).\
        filter(func.strftime("%Y-%m-%d", measurement.date) >= "2016-08-23").all()
        
        tobs_dict = {}
        for result in tobs_data:
            tobs_dict[result[0]] = ({"Station": result[1], "TOBS":result[2]})
        
        return jsonify(tobs_dict)
    
#################################################  

# Return a JSON list of the minimum temperature, the average temperature, 
# and the max temperature for last year with start date.

@app.route("/api/v1.0/2016-08-23")


def start_date():
    
    start_day = session.query(func.strftime("%Y-%m-%d", measurement.date),func.min(measurement.tobs),
                              func.avg(measurement.tobs), func.max(measurement.tobs)).filter(
                                measurement.date >= "2016-08-23").\
                                group_by(measurement.date).all()    
    temps_dict= {}
    for result in start_day:
        temps_dict[result[0]] = ({"Min. (F°)":result[1], "Average (F°)": (round(result[2], 1)),
                                  "Max. (F°)": result[3]})
        
    return jsonify(temps_dict)
    
#################################################  

if __name__ == '__main__':
    app.run(debug=True)

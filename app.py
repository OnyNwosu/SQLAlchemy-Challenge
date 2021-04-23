# Import dependencies
from flask import Flask, render_template, request, redirect, jsonify
import numpy as np 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

# SET UP FLASK APP
app = Flask(__name__)

#SET UP DATABASE & DB REFERENCES
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# CREATE FLASK ROUTES
@app.route("/")
def home():
    homepageHTML = (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end"
    )
    return homepageHTML

@app.route("/api/v1.0/precipitation") 
def precipitation():
    # Create session
    session = Session(engine)

    precipitation_data = session.query(func.strftime("%Y-%m-%d", Measurement.date), Measurement.prcp).filter(func.strftime("%Y-%m-%d", Measurement.date) >= dt.date(2016, 8, 23)).all()

    # Close session
    session.close()
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    # Create session
    session = Session(engine)
    active_stations = (session.query(Measurement.station, Station.name, func.count(Measurement.id)).filter(Measurement.station == Station.station).group_by(Measurement.station).order_by(func.count(Measurement.id).desc()).all())

    # Close session
    session.close()
    return jsonify(active_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create session
    session = Session(engine)
    first_date = session.query(Measurement.date).order_by(Measurement.date).first()
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = session.query(func.max(func.strftime("%Y-%m-%d", Measurement.date))).limit(5).all()
    last_date[0][0]
    active_stations = (session.query(Measurement.station, Station.name, func.count(Measurement.id)).filter(Measurement.station == Station.station).group_by(Measurement.station).order_by(func.count(Measurement.id).desc()).all())
    station_record = (session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs),).filter(Measurement.station == active_stations[0][0]).all())    
    most_active = 'USC00519281'
    year_temps = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active).\
    filter(func.strftime("%Y-%m-%d", Measurement.date) >= dt.date(2016, 8, 23)).all()

    # Close session
    session.close()
    return jsonify(station_record)

@app.route("/api/v1.0/temp/start")
def start(start='01-01-2010'):
    #01/01/2010 = start
    # Create session
    session = Session(engine)
    start_only = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    
   
    # Close session
    session.close()
    return jsonify(start_only)


@app.route("/api/v1.0/temp/start/end")
def start_and_end(start='MM-DD-YYYY', end='MM-DD-YYYY'):
    #08/23/2017 = end
    # Create session
    session = Session(engine)
    start_and_end = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
   

    # Close session
    session.close()
    return jsonify(start_and_end)
    

if __name__ == '__main__':
    app.run(debug=True) # set to false if deploying to live website server
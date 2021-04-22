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

    # YOUR CODE HERE
    precipitation_data = session.query(func.strftime("%Y-%m-%d", Measurement.date), Measurement.prcp).filter(func.strftime("%Y-%m-%d", Measurement.date) >= dt.date(2016, 8, 23)).all()
    # YOUR CODE HERE

    # Close session
    session.close()
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    # Create session
    session = Session(engine)
    
    # YOUR CODE HERE
    # YOUR CODE HERE

    # Close session
    session.close()
    return "Calculations for STATIONS"

@app.route("/api/v1.0/tobs")
def tobs():
    # Create session
    session = Session(engine)
    
    # YOUR CODE HERE
    # YOUR CODE HERE

    # Close session
    session.close()
    return "Calculations for TOBS"

@app.route("/api/v1.0/<start>")
def start(start='MM-DD-YYYY'):
    # Create session
    session = Session(engine)
    
   
   

    # Close session
    session.close()
    return "Calculations for START DATE"

@app.route("/api/v1.0/<start>/<end>")
def start_and_end(start='MM-DD-YYYY', end='MM-DD-YYYY'):
    # Create session
    session = Session(engine)
    
   
    

    # Close session
    session.close()
    return "Calculations for START & END DATES"

if __name__ == '__main__':
    app.run(debug=True) # set to false if deploying to live website server
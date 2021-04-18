# Import dependencies
from flask import Flask, render_template, request, redirect, jsonify
import numpy as np 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# SET UP DATABASE

# Create enginge
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect database
Base = automap_base()
# Reflect tables
Base.prepare(engine, reflect=True)

# CREATE FLASK APP

# Create an instance 
app = Flask(__name__)

# CREATE FLASK ROUTES


@app.route("/")
def home():
    # Create session
    session = Session(engine)
    # Close session
    session.close()
    return "This webpage is under construction."

@app.route("/api/v1.0/precipitation  ") 
def precipitation():
    # Create session
    session = Session(engine)
    # Close session
    session.close()
    return "This webpage is under construction."

@app.route("/api/v1.0/stations")
def stations():
    # Create session
    session = Session(engine)
    # Close session
    session.close()
    return "This webpage is under construction."

@app.route("/api/v1.0/tobs")
def tobs():
    # Create session
    session = Session(engine)
    # Close session
    session.close()
    return "This webpage is under construction."

@app.route("/api/v1.0/<start>")
def start():
    # Create session
    session = Session(engine)
    # Close session
    session.close()
    return "This webpage is under construction."

@app.route("/api/v1.0/<start>/<end>")
def end():
    # Create session
    session = Session(engine)
    # Close session
    session.close()
    return "This webpage is under construction."

if __name__ == '__main__':
    app.run()
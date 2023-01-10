import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask


##database
engine = create_engine("sqlite://Resources/hawaii.sqlite")

##existing database
Base = automap_base()
Base.prepare(engine, reflect=True)

session = Session(engine)
##reference
Measurement = Base.classes.measurement
Station = Base.classes.station

##last date in db
last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

##12 months from last date
query_date = dt.date(2017-8-23) - dt.timedelta(days=365)

session.close()

##app
app = Flask(__name__)

















if __name__ == "__main__":
    app.run(debug=True)
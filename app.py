
from flask import Flask , render_template, request

import numpy as np
import pandas as pd
import model as m 
import os


app=Flask(__name__)



@app.route("/", methods= ["GET","POST"]) 

def model():
    
    tp=0
    #global tp
    if request.method == "POST":
        ApparentTemperature=request.form["ApparentTemperature"]
        Humidity=request.form["Humidity"]
        WindSpeed=request.form["WindSpeed"]
        WindBearing=request.form["WindBearing"]
        Visibility=request.form["Visibility"]
        LoudCover=request.form["LoudCover"]
        Pressure=request.form["Pressure"]

        temp_pred=m.temp_prediction(ApparentTemperature,Humidity,WindSpeed,WindBearing,Visibility,LoudCover,Pressure)
        tp = temp_pred
    return render_template("form.html", my_temp = tp)
    


#@app.route("/")
#def submit():
#return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)

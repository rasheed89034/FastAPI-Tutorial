# CCTV surveillance system

from fastapi import FastAPI

app = FastAPI()

@app.post("/submit_alert")
def cameraData(camera_id : int , anomaly_type : str, location : str):
    return{
        "Camera Id is = " : camera_id,
        "Anomaly Type is = " : anomaly_type,
        "Location" : location
    }

@app.get("/alert")
def getData(severity : str = "High"):
    return{
        "Severity value is = " : severity
    }

## Make it smart
@app.post("/anomaly")
def checkData(camera_id : int , anomaly_type : str, location : str):
    danger = ["fire","smoke","fighting"]

    if anomaly_type.lower() in danger:
        return{
            "Status":anomaly_type,
            "Message": "Emergancey Alert 🚨",
            "Location":location
        }
    else:
        return{
            "Camera Id is = " : camera_id,
            "Anomaly Type is = " : anomaly_type,
            "Location" : location 
        }
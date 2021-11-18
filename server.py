import flask
import os

#############################################
## This function sets up the app object
## 
#############################################

def create_app(name):
    ## Create APP Object
    app = flask.Flask(name)
    return app

## Create App Object
app = create_app(__name__)


## Create a Route
@app.get("/")
def home():
    return {"response": "Hello World"}

@app.get("/cheese")
def cheese():
    return {"response": "gouda"}

## Run Application
if (__name__ == "__main__"):
    app.run(port=os.environ.get("PORT", 4000))
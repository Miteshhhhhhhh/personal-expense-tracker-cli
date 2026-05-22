#FLASK IS WEB FRAMEWORK FOR PYTHON
# WE CAN CREATE AN API USING IT like WEB API OR WEB BECKEND
#CREATING A FIRST "TO-DO API" IN PYTHON
from flask import Flask

data = {
    "1": {"task": "Learn python", "done" : False},
    "2": {"task": "Create API", "done" : False}
}
app = Flask(__name__)
@app.route("/todos", method = "GET")
def get_todos():
    response = []
    for key, value in data.items():
        temp = value
        temp["Id"] = key
        response.append(temp)
    return response



if __name__ == "__Flask&API__":
    app.run(debug=True)

from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
        </style>
    </head>
    <body>
        <form method= "POST">
         <div>
            <label for= "rot"> Rotate by:</label>
            <input name = "rot" value = "0" type= "text"/>
        </div>
            <label>
                <textarea type = "text" name= "text">{0}</textarea>
            </label>
            <br>
            <label>
            <input type= "submit"/>
            </label>
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form["rot"] 
    rot = int(rot)
    text = request.form["text"]
    rot_text = rotate_string(text,rot)
    return form.format(rot_text)

app.run()
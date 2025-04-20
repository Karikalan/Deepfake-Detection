from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def awareness():
    return render_template("awareness.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return render_template("result.html", result="No file uploaded!")

    file = request.files["file"]
    if file.filename == "":
        return render_template("result.html", result="No file selected!")

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    return render_template("result.html", result="File uploaded successfully!")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
from flask import Flask, render_template, request, url_for
import requests
import os
from flask import request as req

from dotenv import load_dotenv
load_dotenv()

os.getenv("HF_TOKEN")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if req.method == "POST":
        API_URL = "https://router.huggingface.co/hf-inference/models/sshleifer/distilbart-cnn-12-6"
        headers = {
            "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
        }

        data = req.form["data"]
        maxL = int(req.form["maxL"])
        minL = maxL//4

        def query(payload):
            
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},
        })[0]

        return render_template("index.html", result=output["summary_text"])
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()

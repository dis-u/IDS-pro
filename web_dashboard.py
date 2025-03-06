from flask import Flask, render_template, jsonify

app = Flask(__name__)

alerts = []

@app.route("/")
def dashboard():
    return render_template("index.html", alerts=alerts)

@app.route("/alerts", methods=["GET"])
def get_alerts():
    return jsonify({"alerts": alerts})

@app.route("/add_alert/<msg>")
def add_alert(msg):
    alerts.append(msg)
    return "Alert added"

if __name__ == "__main__":
    app.run(debug=True, host="192.168.142.92", port=5000)

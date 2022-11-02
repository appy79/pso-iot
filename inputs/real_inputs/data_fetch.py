from flask import jsonify, request

from . import app


@app.route("/input", methods=["POST"])
def incoming_data():
    return jsonify()


@app.route("/output", methods=["GET"])
def outgoing_data():
    return jsonify()

from flask import Flask, jsonify

# setup

app = Flask(__name__)


# routes
import inputs.real_inputs.data_fetch

# run
if __name__ == "__main__":
    app.run(debug=True)

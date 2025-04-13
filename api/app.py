import os
from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/api/v1.0/test', methods=['GET'])
def test_response():
    """Return a sample JSON response."""
    sample_response = {
        "items": [
            { "id": 1, "name": "Apples",  "price": "$2"},
            { "id": 2, "name": "Peaches", "price": "$5"}
        ]
    }
    # JSONify response
    response = make_response(jsonify(sample_response))

    # Add Access-Control-Allow-Origin header to allow cross-site request
    response.headers['Access-Control-Allow-Origin'] = 'https://discover.test.elastiq.app'

    # Mozilla provides good references for Access Control at:
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control

    return response


@app.route('/', methods=['GET'])
def health():
    """Return a sample JSON response."""
    sample_response = {
        "health": "ok"
    }
    response = make_response(jsonify(sample_response))
    response.headers['Access-Control-Allow-Origin'] = 'https://discover.test.elastiq.app/'
    return response


if __name__ == "__main__":
    PORT = os.getenv('PORT', 5000)
    app.run(debug=True, host="0.0.0.0", port=PORT)

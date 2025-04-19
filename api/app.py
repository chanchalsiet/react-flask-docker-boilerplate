import os
from flask import Flask, jsonify, make_response
from google.cloud import storage
app = Flask(__name__)


@app.route('/api/v1.0/test', methods=['GET'])
def test_response():
    """Return a sample JSON response."""
    sample_response = {
        "items": [
            {"id": 1, "name": "Apples",  "price": "$2"},
            {"id": 2, "name": "Peaches", "price": "$5"},
            {"id": 3, "name": "Grapes", "price": "$50"},
            {"id": 4, "name": "Papya", "price": "$150"},
            {"id": 5, "name": "cherry", "price": "$250"},
            {"id": 6, "name": "berry", "price": "$150"},
            {"id": 7, "name": "berry1", "price": "$100"},

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


@app.route('/api/v1.0/gcs/<bucket_name>', methods=['GET'])
def test_gcs(bucket_name):
    """Return a sample JSON response."""
    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    # Note: The call returns a response only when the iterator is consumed.
    names = []
    for blob in blobs:
        names.append(blob.name)
    return jsonify(names)


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

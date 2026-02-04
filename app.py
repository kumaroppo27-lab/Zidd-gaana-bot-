import os
from flask import Flask, jsonify

app = Flask(__name__)

# Health check endpoint (important for Render)
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/")
def hello():
    return "Hello VenomX - Server is running!"

# Another endpoint to test
@app.route("/api/test")
def test():
    return jsonify({"message": "API is working", "status": "success"})

# 404 error handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

# 500 error handler
@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    # Disable debug mode in production
    app.run(host="0.0.0.0", port=port, debug=False, threaded=True)

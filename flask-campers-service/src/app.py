from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def health():
        return jsonify({"status": "ok"}), 200
    return app

if __name__ == "__main__":
    app = create_app()
    # Run on port 5555 to match the challenge instructions
    app.run(port=5555, debug=True)
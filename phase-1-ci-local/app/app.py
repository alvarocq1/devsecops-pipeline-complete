from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    api_key = "1234567890abcdef"  # Secret hardcoded (deliberate vuln)
    return f"Hello, world! Your IP is {request.remote_addr}"

if __name__ == '__main__':
    app.run(debug=True)

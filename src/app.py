from flask import Flask
import speedtest

app = Flask(__name__)

@app.route("/")
def index():
    st = speedtest.Speedtest()
    return "Hello, world!"



if __name__ == "__main__":
    app.run()

import speedtest
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # st = speedtest.Speedtest()
    # download = st.download()
    return "Hello, world! "



if __name__ == "__main__":
    app.run()

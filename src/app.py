import speedtest
from flask import Flask

app = Flask(__name__)
st = speedtest.Speedtest()

@app.route("/")
def index():
    return "Hello, world! " + str(st.download()/1_000_000)



if __name__ == "__main__":
    app.run()

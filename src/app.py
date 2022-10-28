import speedtest
from flask import Flask

app = Flask(__name__)
st = speedtest.Speedtest()

@app.route("/")
def index():
    return f'Download Speed: {round(st.download()/1_000_000, 1)} Mb/s'



if __name__ == "__main__":
    app.run()

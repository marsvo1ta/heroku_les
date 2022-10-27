from flask import Flask
import speedtest

app = Flask(__name__)

@app.route("/")
def index():
    st = speedtest.Speedtest()
    download = st.download()
    return "Hello, world! " + str(download/1_000_000)



if __name__ == "__main__":
    app.run()

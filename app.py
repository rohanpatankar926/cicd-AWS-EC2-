from flask import Flask
app=Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return "<h1>Hello World</h1>"

if __name__=="__main__":
    app.run(host="127.0.01",port=8000)

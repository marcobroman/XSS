from flask import Flask,request

app=Flask(__name__)

@app.route("/")
def index():
    item = request.args.get("item","default")

    if request.method == "GET":
        return item
    
if __name__ == "__main__":
    app.run(debug=True)
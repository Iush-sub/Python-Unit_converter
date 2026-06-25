from flask import Flask,render_template,request,redirect


app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        from_unit= request.form["from_unit"]
        to_unit= request.form["to_unit"]

        value = float(request.form["value"])
        result = convert(
            value,
            from_unit,
            to_unit
        )

    return render_template("index.html", test=result)


def convert(value,from_unit,to_unit):

    if from_unit == "meter" and to_unit == "kilometer":
        return value/1000
    elif from_unit == "kilometer" and to_unit == "meter":
        return value * 1000

    return value





if __name__ == '__main__':
    app.run(debug=True,port=8000) #using 8000 to look aesthetic
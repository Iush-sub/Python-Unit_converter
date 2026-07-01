from flask import Flask,render_template,request,redirect
from converter import conv #importaing distance conv function from converter py file
from converters.weight import convert_weight


app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        from_unit= request.form["from_unit"] #its stores the conversion part
        to_unit= request.form["to_unit"]# same goes for this
        category= request.form["category"]
        value = float(request.form["value"])# stores the numeric value from website as float
        if category == "length":
            result = conv(value, from_unit, to_unit)

        elif category == "weight":
            result = convert_weight(
                value,
                from_unit,
                to_unit
            )

        elif category == "temperature":
            result = None

        elif category == "time":
            result = None

    return render_template("index.html", test=result) #here test is a variable in website which holds the value of variable result in python








if __name__ == '__main__':
    app.run(debug=True,port=8000) #using 8000 to look aesthetic
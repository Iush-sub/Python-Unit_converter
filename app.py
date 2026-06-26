from flask import Flask,render_template,request,redirect
from converter import distance_conv #importaing distance conv function from converter py file



app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        from_unit= request.form["from_unit"] #its stores the conversion part
        to_unit= request.form["to_unit"]# same goes for this

        value = float(request.form["value"])# stores the numeric value from website as float
        result = distance_conv(
            value,
            from_unit,
            to_unit
        )

    return render_template("index.html", test=result) #here test is a variable in website which holds the value of variable result in python








if __name__ == '__main__':
    app.run(debug=True,port=8000) #using 8000 to look aesthetic
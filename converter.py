length_unit = {
    "meter": 1,
    "kilometer": 1000,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "inch": 0.0254
}

variety= {
    "length":length_unit,
    "Area":{
        "meter sq":1,
        "kilometer sq":1000*1000

    },
    "weight":{
        "gram":0.001,
        "milligram":0.001*0.001,
        "kilogram":1
    }

}





def conv(value,from_unit,to_unit):

    base= value * variety["length"][from_unit]
    ans = base / variety["length"][to_unit]

    return ans #works perfectly

length_unit = {
    "meter": 1,
    "kilometer": 1000,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "inch": 0.0254
}

varrity= {
    "length":length_unit,
    "Area":{
        "meter sq":1,
        "kilometer sq":1000*1000

    }
    "weight":
}





def conv(value,from_unit,to_unit,category):

    base= value * length_unit[from_unit]
    ans = base / length_unit[to_unit]

    return ans #works perfectly

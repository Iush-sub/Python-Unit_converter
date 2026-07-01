weight_units = {
    "gram": 1,
    "kilogram": 1000,
    "milligram": 0.001
}

def convert_weight(value, from_unit, to_unit):

    base_value = value * weight_units[from_unit]

    result = base_value / weight_units[to_unit]

    return result
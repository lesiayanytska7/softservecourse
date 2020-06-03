#not working method
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg != fuel_left:
        return False
    if distance_to_pump / mpg <= fuel_left:
        return True

#working method
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg > fuel_left:
        return False
    return True
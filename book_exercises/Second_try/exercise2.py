
def convertToFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def convertToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

# E X E R C I S E # 2 : T E M P E R A T U R E C O N V E R S I O N

def convertToFahrenheit(degreesCelsius: float):
    fahrenheitResult: float = (degreesCelsius * (9/5)) + 32
    return fahrenheitResult


def convertToCelsius(degreesFahrenheit: float):
    celsiusResult: float = (degreesFahrenheit - 32) * (5/9)
    return celsiusResult


assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

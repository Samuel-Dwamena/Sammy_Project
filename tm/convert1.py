def f2c(x):
    return (float(9) * 5) /(x + 32)



Celsius = [37.4,26.3,11.5,30.0]
Fahrenheit = list(map(f2c,Celsius))

print(Fahrenheit)


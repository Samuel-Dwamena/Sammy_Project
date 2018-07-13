def f(a):
    def g(b,c):
        return a * (b+c)
    return g

x = f(1)
print(x(2,3))

y = f(2)
print(y(2,3))

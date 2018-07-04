import math
import cmath

# z= z*z +num
def mandelbrot(n):
    z = 0
    for nu in range(5):
        z = z*z + nu
        if math.fabs(z) >= 2: # escaped values
            return "->"
        else:
            return "*"
s =""
for x in range(-5,20):
    for y in range (-13,21):
        s += mandelbrot(cmath.phase(complex(x,y)))
    s += "\n"

print(s)
    
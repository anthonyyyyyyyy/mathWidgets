import math

def circle(r):
      pi = 3.141592653589
      Equations = []
      for i in range (0,361):
            i = float(i)
            radians = float((i * pi)/180)
            x = ((math.cos(radians))*r)
            y = ((math.sin(radians))*r)
            if((i > 0) and (i < 180)):
                  der = (0.5*(pow(((r*r)-(x*x)), (-0.5)))*(-2*x))
                  Equations.append("y = " + str(der) + "x + " + str(der*(-x)+y))
            elif((i > 180) and (i <= 359)):
                  der = ((-0.5)*(pow(((r*r)-(x*x)), (-0.5)))*(-2*x))
                  Equations.append("y = " + str(der) + "x + " + str(der*(-x)+y))
            elif((i == 0) or (i == 180)):
                  Equations.append("x = " + str(math.ceil(x)))
            else:
                  del (der, pi, r , radians, x, y)
      return Equations

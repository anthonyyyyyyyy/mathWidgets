import math
class vector:
    def rotate(x, y, angle):
        theta = float(angle/180 * math.pi)
        a, b = math.cos(theta), math.sin(theta)
        return [x*a-y*b,x*b+y*a]

import math
class vector:
    def magnitude(v):
        sum = 0.0
        for i in range(0,len(v)):
            sum = sum + (v[i]**2)
        return sum**0.5
    def normalize(v):
        magnitude = vector.magnitude(v)
        for i in range(0,len(v)):
            v[i] = v[i]/magnitude
        return v
    def rotate(x, y, angle): #2D vector rotations
        theta = float(angle/180.0 * math.pi)
        a, b = math.cos(theta), math.sin(theta)
        return [x*a-y*b,x*b+y*a]
    def dot(u, v): #3D dot products (Set z to 0 for 2D dot product)
        product = 0.0
        for i in range(0,len(u)):
            product = product + (u[i]*v[i])
        return product
    def angle(u, v):
        give = vector.dot(u, v) / (vector.magnitude(u)*vector.magnitude(v))
        return math.acos(give)/math.pi * 180
    def cross(u, v):
        return [u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]

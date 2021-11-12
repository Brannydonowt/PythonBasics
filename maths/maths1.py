# .py file for python maths exercises

# convert degree to radian
# x * pi/180
# in = 15
# out = 0.2619047619047619
def deg2rad(degrees):
    pi = 22/7
    return degrees * pi / 180

# convert radian to degree
# in = .52
# out = 29.781818181818185
def rad2deg(rad):
    pi = 22/7
    return rad / pi * 180

# area of trapezoid
# a = (a+b/2)h
# in = h: 5, a: 5, b: 6
# # out = 27.5
def area_of_trapezoid(a, b, h):
    ab = a + b
    return (ab / 2) * h

# area of parallelogram
# a = bh
# in = b: 5, h: 6
def area_of_parallelogram(b, h):
    return b*h

# surface volume and surface area of cylinder
# a = 2(pi)rh + 2(pi)r^2
# v = (pi)r^2h
# in = h: 4, r: 6
# out a = 377.1428571428571
# out v = 452.57142857142856
def get_volume_surface_of_cylinder(r, h):
    pi = 22/7
    a = (2 *pi) * r * h + (2 * pi) * (r * r)
    print(a)
    v = pi * (r * r) * h
    print (v)
# Checking the collinearity of three points in Cartesian Plane

x1 = float(input("Co-ords of point 1 :"))
y1 = float(input())

x2 = float(input("Co-ords of point 2 :"))
y2 = float(input())

x3 = float(input("Co-ords of point 3 :"))
y3 = float(input())

r = (x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))

if r == 0:
    print("Given points are co-linear")

else:
    print("Given points are not co-linear")

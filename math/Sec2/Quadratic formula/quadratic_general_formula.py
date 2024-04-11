import math
a = int(input("What is your a for ax²"))
b = int(input("What is your b for bx"))
c = int(input("What is your c"))
y_intercept = c
h_vertex = -(b/(2*a))
v_vertex = ((a*(h_vertex**2)) + b*h_vertex + c)
vertex_coordinates = (h_vertex,v_vertex)
print("The vertex coordinates are "+str(vertex_coordinates))
try:
  x_1 = ((-b +(math.sqrt(b**2-4*a*c)))/(2*a))
  x_2 = ((-b -(math.sqrt(b**2-4*a*c)))/(2*a))
  rounded_x_1 = round(x_1,3)
  rounded_x_2 = round(x_2,3)
  x_1_coords = rounded_x_1,0
  x_2_coords = rounded_x_2,0
  x0 = False
except ValueError:
  x0 = True
if x0 is True:
  print("There are no x-intercepts")
elif rounded_x_1 is rounded_x_2:
  print("The x-intercept is"+str(x_1_coords))
else:
  print("The two x-intercepts are "+str(x_1_coords)+" and "+str(x_2_coords))
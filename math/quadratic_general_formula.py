#Note to self: this is parabola also its to get minimum or maximum and the two x intercepts
#c = y intercept
#coords of vertex = h = -(b/2a) where h is x coord then since x coords is h then k = (ah^2 + bh + c) where k = y coords
#vertex = minimum/maximum point or turning/stationary point
#x intercepts = (-b +-(sqrt(b^2-4ac)))/2a
#so for eg. x^2-25=0 a=1, b=0, c=-25 (-0 +-(sqrt(100)))/2 means x1 is 5 and x2 is -5
#done with the help of Microsoft Copilot teaching me the graph
import math
a = int(input("What is your a for ax²"))
b = int(input("What is your b for bx"))
c = int(input("What is your c"))
y_intercept = c
h_vertex = -(b/(2*a))
v_vertex = ((a*(h_vertex**2)) + b*h_vertex + c)
vertex_coordinates = (h_vertex,v_vertex)
print(vertex_coordinates)
x_1 = ((-b +(math.sqrt(b**2-4*a*c)))/(2*a))
x_2 = ((-b -(math.sqrt(b**2-4*a*c)))/(2*a))
rounded_x_1 = round(x_1,3)
rounded_x_2 = round(x_2,3)
x_1_coords = rounded_x_1,0
x_2_coords = rounded_x_2,0
print(x_1_coords,x_2_coords)

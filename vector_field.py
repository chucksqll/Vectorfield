#Drawing simple vector field
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.cm as cm
from matplotlib.colors import Normalize

def draw(name,fir_coord_func, sec_coord_func,area,density,vector_scale,vector_thickness):

    x_left_rng = area[0][0]
    x_right_rng = area[0][1]
    y_left_rng = area[1][0]
    y_right_rng = area[1][1]
    
    x_points = np.arange(x_left_rng - 1, x_right_rng + 1, density)
    y_points = np.arange(y_left_rng - 1, y_right_rng + 1, density)
    
    X, Y = np.meshgrid(x_points, y_points)
    
    x_shape = X.shape

    U = np.zeros(x_shape)
    V = np.zeros(x_shape)
    for j, s in zip(range(x_shape[1]), x_points):
        for i, t in zip(range(x_shape[0]), y_points):
            vector_length = math.sqrt(fir_coord_func(s, t) * fir_coord_func(s, t) + sec_coord_func(s, t) * sec_coord_func(s, t))
            if vector_length == 0:
                U[i,j] = 0
                V[i,j] = 0
            else:
              U[i, j] = fir_coord_func(s, t)
              V[i, j] = sec_coord_func(s, t)
              
              
    fig, ax = plt.subplots(figsize = (5, 5))
    
    #settings arrows
 
    M = np.hypot(U, V)#color
    ax.set_title(name)
    q = ax.quiver(X, Y, U, V, M, units='xy',pivot='tail', scale = vector_scale, width = vector_thickness)
    
    #scalling x y
    ax.set_aspect('equal')
    
    plt.xlim(x_left_rng, x_right_rng)
    plt.ylim(y_left_rng, y_right_rng)
       
    plt.show()
    plt.close()
    
# #------------------------------------------------------#
#draw(area,density,vector_scale,vector_thickness) 
#a  2 dimensional array [[x1,y1],[x2,y2]] which is the area where plot should be drawn
#density density grid
#vector_scale scalling vector the bigger number the smaller vector
#vector_thickness arrows thickness
#fir_coord_func applies function on  first coordinate
#sec_coord_func applies function on  second coordinate
#F(x,y)=(fir_coord_func ,sec_coord_func )
# first_func ->first coordinate
# sec_func ->second coordinate


###EXAMPLE###
#Vector field F(x,y)=(cosx,siny)
######
def first_func(x,y):
    return np.cos(x)
def second_func(x,y):
    return np.sin(y)

draw("Vector field F(x,y)=(cosx,siny)", first_func, second_func,[[-6, 6],[-6, 6]], 0.5 , 1.5 , 0.05)

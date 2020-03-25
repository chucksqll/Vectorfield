# Vectorfield
Drawing vectorfields using matplotlib

Example for F(x,y)=(cosx,siny)

##
def draw(...)
  ...
  
def first_func(x,y):
    return np.cos(x)
    
def second_func(x,y):
    return np.sin(y)

draw("Vector field F(x,y)=(cosx,siny)",first_func,second_func,[[-6,6],[-6,6]],0.5 ,1.5 ,0.05 )
###
will show

![](images/cos(x)siny.png)

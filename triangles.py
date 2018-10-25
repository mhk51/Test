import turtle,sys
n = int(sys.argv[1])
turtle.speed(0)
def triangle(n,length=100):
    if n == 1:
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
    else:
        triangle(n-1,length/2)
        triangle(n-1,length/2)
        turtle.left(120)
        turtle.forward(length/2)
        triangle(n-1,length/2)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        
    
        

triangle(n)
turtle.done()
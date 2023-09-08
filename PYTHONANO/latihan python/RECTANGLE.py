import turtle
def  drawRectangle ( ttl , x , y , width , length ):
     ttl.penup ()
     ttl.goto (x , y)
     ttl.setheading (0)
     ttl.pendown() 
     for count in range (4) : 
         ttl.forward ( width )
         ttl.right ( 120 )
         ttl.forward ( length )
         ttl.pendown ()
         ttl.penup ()

Bob = turtle . Turtle ()
Bob.speed (10)
Bob.pensize (3)
drawRectangle ( Bob , 0, 0, 150, 200 )

turtle . done ()
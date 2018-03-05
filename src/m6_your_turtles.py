"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jeremy Roy.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# Done: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
####################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

trinity = rg.SimpleTurtle('turtle')
trinity.pen = rg.Pen('purple',10)
trinity.speed = 25

size = 400

for k in range(15):
    trinity.draw_regular_polygon(6,size)

    trinity.pen_up()
    trinity.right(45)
    trinity.forward(20)
    trinity.left(45)

    trinity.pen_down()

    size= size - 15

anna = rg.SimpleTurtle()
anna.pen = rg.Pen("green", 5)
anna.speed = 10

anna.backward(175)

size = 10

for k in range(29):
    anna.draw_regular_polygon(10,size)

    anna.pen_up()
    anna.left(90)
    anna.backward(15)
    anna.right(90)

    anna.pen_down()

    size = size + 1

window.close_on_mouse_click()
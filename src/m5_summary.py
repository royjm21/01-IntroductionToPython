"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jeremy Roy.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   Write code that constructs a SimpleTurtle with a red Pen
#   and makes it move around a bit.  Don't forget to:
#     -- import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     -- ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

jeff = rg.SimpleTurtle('turtle')

jeff.pen = rg.Pen('red',5)
jeff.speed = 20
jeff.forward(150)
jeff.left(90)
jeff.forward(150)
jeff.left(90)
jeff.forward(150)
jeff.left(90)
jeff.forward(150)

jeff.pen = rg.Pen('blue',10)

jeff.forward(150)
jeff.left(90)
jeff.forward(150)
jeff.left(90)
jeff.forward(150)

window.close_on_mouse_click()
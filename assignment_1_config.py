
#-----Module Description - Drawing Canvas Configuration--------------#
#
#  This module contains functions needed for Assignment 1 in QUT's
#  teaching unit IFB104 "Building IT Systems".  You should put
#  a copy of this file in the same folder as your solution to the
#  assignment.  The necessary elements will then be imported
#  into your program automatically.
#
#  NB: Do NOT make any changes to this module and do NOT submit a
#  copy of this file with your solution.  Changes made to this
#  module will have no effect when your assignment is graded because
#  the markers will use their own copy of the file.  If your program
#  relies on changes made to this file it will fail to work when
#  assessed.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section defines constants and imports functions used for
# creating the drawing canvas.
#

# Import standard Python functions needed to support this module.
from turtle import *
from math import *

# Define the length of the sides of the cells. All other dimensions
# for the drawing canvas are calculated relative to this value.
cell_side = 60 # pixels

# Define the overall size of our "flat top" hexagonal grid
grid_width = 9 # hexagonal cells
grid_height = 9 # hexagonal cells

# To ensure that the grid has a cell at the centre, the arithmetic
# below supports only certain grid sizes
assert [grid_width, grid_height] in \
       [[5, 5],  [9, 5],   [13, 5],
        [7, 7],  [11, 7],  [15, 7],
        [5, 9],  [9, 9],   [13, 9],
        [7, 11], [11, 11], [15, 11],
        [5, 13], [9, 13],  [13, 13]], 'Invalid grid dimensions'

# Derive constant values used in the main program that sets up
# the drawing canvas.
cell_width = cell_side * 2 # cell width for a grid with "flat top"
                           # orientation
cell_height = round(2 * (cell_side * sin(radians(60)))) # cell height and
                                                        # distance from neighbours
horiz_spacing = round(3 / 4 * cell_width) # distance between grid cells
                                          # horizontally
vert_spacing = cell_height / 2 # distance between grid cells
                               # vertically
x_margins = horiz_spacing * 5.5 # the total size of the margins left
                                # and right of the grid
y_margins = vert_spacing * 4 # the total size of the margins below
                             # and above the grid
window_height = int(((grid_height + 1) * vert_spacing) + y_margins) # the drawing
                                                                    # canvas' height
window_width = int((grid_width * horiz_spacing) + x_margins) # the drawing
                                                             # canvas' width
coord_font = ('Arial', cell_side // 3, 'normal') # text font for labels
                                                 # on grid axes
label_font = ('Arial', cell_side // 2, 'normal') # text font for
                                                 # instructions

#
#--------------------------------------------------------------------#



#-----Functions for Maintaining the Drawing Canvas-------------------#
#
# The functions in this section are called by the assignment template
# to manage the drawing canvas used by your program.
#

# Set up the canvas and draw the background for the overall image
#
def create_drawing_canvas(canvas_title = "Put your solution's title here",
                          bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          write_instructions = True):
    
    # Set up the drawing canvas with enough space for the grid and
    # margins
    setup(window_width, window_height)
    bgcolor(bg_colour)
    title(canvas_title)

    # Draw the canvas as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid (defined
    # as the left-most point of the bottom-left cell)
    left_edge = -(((grid_width // 2) * horiz_spacing) + (0.5 * cell_width))
    bottom_edge = -((grid_height - 1) // 2) * vert_spacing
    goto(left_edge, bottom_edge)

    # Optionally draw the grid
    if draw_grid:
        # Draw the cells row by row
        for rows in range(ceil(grid_height / 2)):
            # Draw upper half of row
            goto(left_edge, bottom_edge + (rows * cell_height))
            pendown()
            setheading(0) # face east
            for angle in ([60, -60, -60, 60] * ceil(grid_width / 2))[:-1]:
                left(angle)
                forward(cell_side)
            penup()
            # Draw lower half of row
            goto(left_edge, bottom_edge + (rows * cell_height))
            pendown()
            setheading(0) # face east
            for angle in ([-60, 60, 60, -60] * ceil(grid_width / 2))[:-1]:
                left(angle)
                forward(cell_side)
            penup()

        # Label the x axis
        penup()
        y_offset = cell_height // 1.2 # pixels
        for x_label in range(grid_width):
            goto(left_edge - (cell_width // 4) + ((x_label + 1) * (cell_width // 1.32)),
                 bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = coord_font)

        # Label the y axis
        penup()
        x_offset, y_offset = cell_side * 0.7, cell_height // 10 # pixels
        for y_label in range(grid_height):
            goto(left_edge + (horiz_spacing * grid_width) + x_offset,
                 bottom_edge + (y_label * (cell_height // 2)) - y_offset)
            write(str(y_label + 1), align = 'left', font = coord_font)

        # Mark the four "special" cells (assuming a grid
        # of size at least 9 x 9)
        home()
        dot(cell_side // 4) # middle
        home()
        forward(3 * horiz_spacing)
        left(90)
        forward(vert_spacing)
        dot(cell_side // 4) # right
        home()
        left(180)
        forward(horiz_spacing)
        right(90)
        forward(3 * vert_spacing)
        dot(cell_side // 4) # left, top
        home()
        left(180)
        forward(4 * horiz_spacing)
        left(90)
        forward(2 * vert_spacing)
        dot(cell_side // 4) # left, bottom

    # Optionally write instructions for the programmer
    if write_instructions:
        # Write to the left of the grid
        goto(-((grid_width / 1.8) * horiz_spacing), -(vert_spacing // 0.7))
        write('Replace\nthis with\nhalf of\nyour\nsymbol’s\nvariants',
              align = 'right', font = label_font)
        # Write to the right of the grid
        goto((grid_width / 1.7) * horiz_spacing, -(vert_spacing // 0.7))
        write('Replace\nthis with\nthe rest\nof your\nsymbol’s\nvariants',
              align = 'left', font = label_font)
        # Write above the grid
        goto(0, 2 * vert_spacing * (grid_height / 3.2))
        write('Replace this with your final message',
              align = 'center', font = label_font)
        
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)
       


# End the program and release the drawing canvas back to the
# host operating system
#
def release_drawing_canvas(signature,
                           text_colour = 'slate grey'):
    
    # Ensure any student drawing still in progress is displayed
    # completely
    tracer(True)
        
    # Sign the canvas with the student's name
    signature_font = ('Comic Sans MS', cell_side // 3, 'bold')
    color(text_colour)
    penup()
    goto((horiz_spacing * grid_width) / 2,
         -(((grid_height - 1) // 2) + 2.4) * vert_spacing)
    write('Visualisation by ' + signature,
          align = 'right', font = signature_font)    
    
    # Hide the cursor and release the window to the host
    # operating system
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#

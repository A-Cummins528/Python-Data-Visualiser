
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2023.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 11619791
student_name   = ('Adam Cummins')
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
if isfile('assignment_1_config.py'):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print("\nCannot find file 'assignment_1_config.py', aborting!\n")
    abort()

# Define the function for generating data sets, using the
# imported raw data generation function if available, but
# otherwise creating a dummy function that just returns an
# empty list
if isfile('assignment_1_data_source.py'):
    print('Data generation module found ...\n')
    from assignment_1_data_source import raw_data
    def data_set(new_seed = randint(0, 99999)):
        print('Using random number seed', new_seed, '...\n')
        seed(new_seed) # set the seed
        return raw_data() # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#

# All of your code goes in, or is called from, this function.
# Make sure that your code does NOT call function data_set (or
# raw_data) because it's already called in the main program below.



def visualise_data(random_moves):
    tracer(0)
    speed('fastest')

    # Print the 6 different representations on the sides of the screen
    Print_magpie_demonstration()

    # Constants
    x_pos = 0
    y_pos = 0
    step_number = 0 # Keep track of how many steps taken
    
    # Start in the middle and face the initial direction
    # Only the initial instruction uses Magpie because
    # It takes the initial direction from random_moves[0][2]
    # All following steps use Magpie_moves
    Magpie(x_pos,y_pos,random_moves [0][2])
    
    # First check if the bird has enough energy to move
    # If bird does not have enough energy, print a message to the screen      
    if random_moves [0][1] == 0:
        Print_text(0,400,'The bird was too exhaused to fly!')
   
    # Otherwise, move one step and change direction
    # Until the brid has run out of energy
    else:
        # This is the first 'step' from the middle
        forward(cell_height)
        current_heading = heading()
        for Energy in range(random_moves[0][1]):
            step_number = step_number + 1 # Update step counter
            x_pos, y_pos = (pos()) # Update current coordinates
            
            # Checking if the bird has flow off the grid
            if ((x_pos) >= (5 * (0.75 * cell_width))) \
               or ((x_pos) <= (5 * (-0.75 * cell_width))) \
               or ((y_pos) >= (5 * (0.48 * cell_height))) \
               or ((y_pos) <= (5 * (-0.48 * cell_height))):
                    too_far = 'The bird flew away after '+ str(step_number)+' steps!'                       
                    Print_text(0,400,too_far)
                    break

                # Looking for special cell on the right
            elif ((x_pos) >= 270) and ((x_pos) <= 271) and ((y_pos) >= 52) and ((y_pos) <= 53):
                Magpie_moves(x_pos,y_pos,random_moves [Energy+1][1]) # Draw a bird in the cell
                # Print a message saying you have found the right special cell
                special_steps = 'Found a special cell after '+ str(step_number)+' steps!'
                Print_text(0,400,special_steps)
                break

                # Looking for special cell at the bottom left
            elif ((x_pos) == -360)  and ((y_pos) == -104.42):
                Magpie_moves(x_pos,y_pos,random_moves [Energy+1][1]) # Draw a bird in the cell
                # Print a message saying you have found the right special cell
                special_steps = 'Found a special cell after '+ str(step_number)+' steps!'
                Print_text(0,400,special_steps)
                break
            
                # Looking for special cell at the top left
            elif ((x_pos) <= -90) and ((x_pos) >= -91):
                Magpie_moves(x_pos,y_pos,random_moves [Energy+1][1]) # Draw a bird in the cell
                # Print a message saying you have found the right special cell
                special_steps = 'Found a special cell after '+ str(step_number)+' steps!'
                Print_text(0,400,special_steps)
                break

                # Check if bird has run out of energy
            elif step_number == random_moves [0][1]:
                # Print a message saying the bird has run out of energy
                steps = 'The bird became exhausted after '+ str(step_number)+' steps!'
                Magpie_moves(x_pos,y_pos,random_moves [Energy+1][1]) # Draw a bird in the cell
                Print_text(0,400,steps)
                break
            
                # If none of the above conditions have been met, repeat and move forward
            else:
                Magpie_moves(x_pos,y_pos,random_moves [Energy+1][1]) # Draw a bird in the cell
                forward(cell_height) # Move into the next cell, ready to print


# Define a function to turn an input string into a direction
# So that we can take heading instructions from random_moves
# The result is an interger that we can use
# To turn left/right by X degrees        
def heading_interger(input_string):
    if input_string == 'North':
        return 90
    elif input_string == 'North west':
        return 150
    elif input_string == 'North east':
        return 30
    elif input_string == 'South':
        return 270
    elif input_string == 'South west':
        return 210
    elif input_string == 'South east':
        return 330 
    elif input_string == 'Move & turn left':
        return 60    
    elif input_string == 'Move & turn right':
        return -60
    elif input_string == 'Move forward':
        return 0
    

# Print and label 6 Magpies in different directions
# For the demonstration on side of screen
def Print_magpie_demonstration():
    tracer(1) #################
    Magpie(-550,155,'North')
    Print_text(-550,155,'North')
    
    Magpie(-550,0,'North west')
    Print_text(-550,0,'North west')
    
    Magpie(-550,-155,'South west')
    Print_text(-550,-155,'South west')
    
    Magpie(550,155,'South')
    Print_text(550,155,'South')
    
    Magpie(550,0,'South east')
    Print_text(550,0,'South east')
    
    Magpie(550,-155,'North east')
    Print_text(550,-155,'North east')
    tracer(1)
    return Print_magpie_demonstration


# Calling this will draw the hexagon at the current location
# This is used inside the Magpie function
def Hexagon(color): 

    # Some constants 
    cell_side = 60 
    pencolor('black')
    pensize(3)
    fillcolor(color)
    penup()
   
    # Draw the hexagon   
    left(90)
    forward(52) # Height from the middle of cell to the top of cell
    left(90)
    pendown()
    begin_fill()
    forward(cell_side * 0.5) 
    left(60)

    # If you want to draw a different shape, change this value
    for sides in range(5): 
        forward(cell_side) 
        left(60)

    forward(cell_side * 0.5) # This closes the hexagon
    penup()
    left(90)
    forward(51.962) 
    left(90)
    end_fill()
    right
    return Hexagon


# Draw the first Magpie in the centre of the grid
# Facing the initial direction provided by random_moves
def Magpie(x_pos, y_pos,input_string): 
    
    # Some constants
    penup()
    wing_diameter = 80 # The diameter of the bird's wings
    wing_angle = 180 # The distance of the wings streched out straight
    pencolor('black')
    pensize(3)
    goto(x_pos, y_pos)
    
    # This orientates the bird according to the initial value
    # Found in random_moves [0][2]
    setheading(heading_interger(input_string))
    left(90)
    Hexagon('palegreen1')
  
    # Draw the wings
    pensize(2)
    pendown()
    fillcolor('white')
    begin_fill()
    forward(40)
    left(90)
    circle(wing_diameter // 2,extent = wing_angle)
    left(90)
    forward(40)
    end_fill()

    # Draw a second layer of black wings to give more detail
    forward(20)
    fillcolor('black')
    begin_fill()
    left(90)
    circle(wing_diameter // 4, extent = wing_angle)
    left(90)
    forward(20)
    end_fill()

    # Draw the tail shape
    fillcolor('white')
    begin_fill()
    left(60)
    forward(50)
    left(120)
    forward(50)
    left(120)
    forward(50)
    right(30) 
    end_fill()

    # Draw the feathers
    left(125)
    forward(40)
    left(180)
    forward(40)
    left(55) 
    right(125)
    forward(40)
    right(180) 
    forward(40)
    right(55)
    penup()

    # Draw the head and eyes
    forward(10)
    dot (wing_diameter // 3)
    right(90)
    forward(5)
    dot(wing_diameter // 8, 'white')
    dot(wing_diameter // 13)
    right(180)
    forward(10)
    dot(wing_diameter // 8, 'white')
    dot(wing_diameter // 13)

    # Draw the beak
    left(180)
    forward(5) 
    left(90)
    forward(30) 
    right(205) 
    fillcolor('grey')
    begin_fill()
    pendown()
    forward(25) 
    left(115)
    forward(21)
    left(115)
    forward(25)
    end_fill()
    left(155)
    forward(30)
    penup()
    
    # Draw the tail feathers
    forward(10)
    pendown()
    forward(40)
    penup()
    left(180)
    forward(40)

    # End the drawing
    hideturtle()
    return Magpie

def Magpie_moves(x_pos, y_pos,input_string):
    
    # Some constants
    penup()
    wing_diameter = 80 # The diameter of the bird's wings
    wing_angle = 180 # The distance of the wings streched out straight
    pencolor('black')
    pensize(3)
    goto(x_pos, y_pos)
 
   # The key difference between Magpie and Magpie_moves
   # Is that Magpie_moves uses a left instruction below
   # Instead of setheading.
   # This enables us to not be bound to a fixed orientation
    left(heading_interger(input_string))
    left(90)
    Hexagon('palegreen1')

    # Draw the wings
    pensize(2) 
    pendown()
    fillcolor('white')
    begin_fill()
    forward(40)
    left(90)
    circle(wing_diameter // 2,extent = wing_angle)
    left(90)
    forward(40)
    end_fill()

    # Draw a second layer of black wings to give more detail
    forward(20)
    fillcolor('black')
    begin_fill()
    left(90)
    circle(wing_diameter // 4, extent = wing_angle)
    left(90)
    forward(20)
    end_fill()

    # Draw the tail shape
    fillcolor('white')
    begin_fill()
    left(60)
    forward(50)
    left(120)
    forward(50)
    left(120)
    forward(50)
    right(30) 
    end_fill()

    # Draw the feathers
    left(125)
    forward(40)
    left(180)
    forward(40)
    left(55) 
    right(125)
    forward(40)
    right(180) 
    forward(40)
    right(55)
    penup()

    # Draw the head and eyes
    forward(10)
    dot (wing_diameter // 3)
    right(90)
    forward(5)
    dot(wing_diameter // 8, 'white')
    dot(wing_diameter // 13)
    right(180)
    forward(10)
    dot(wing_diameter // 8, 'white')
    dot(wing_diameter // 13)

    # Draw the beak
    left(180)
    forward(5) 
    left(90)
    forward(30) 
    right(205) 
    fillcolor('grey')
    begin_fill()
    pendown()
    forward(25) 
    left(115)
    forward(21)
    left(115)
    forward(25)
    end_fill()
    left(155)
    forward(30)
    penup()
    
    # Draw the tail feathers
    forward(10)
    pendown()
    forward(40)
    penup()
    left(180)
    forward(40)

    # End the drawing
    hideturtle()
    return Magpie_moves


# This will print text to the canvas just below the y_pos
# Use the same x and y pos as the Magpie to label
# The 6 demonstration Magpies
def Print_text(x_pos, y_pos, lable):
    goto(x_pos, y_pos - 80) 
    write(lable, align='center', font=("Arial", 15, "normal"))  
    return Print_text

#
#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas('Magpie', 'light grey', 'slate grey',True,False)

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set(7292)) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#

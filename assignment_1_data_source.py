
#-----Module Description - Data Set Generation-----------------------#
#
#  This module contains a function needed for Assessment Task 1 in
#  QUT's teaching unit IFB104 "Building IT Systems".  You should put
#  a copy of this file in the same folder as your solution to the
#  assignment.  The necessary element will then be imported
#  into your program automatically.
#
#  NB: Do NOT make any changes to this module and do NOT submit a
#  copy of this file with your solution.  Changes made to this
#  module will have no effect when your assignment is graded because
#  the markers will use their own copy of this file.  If your program
#  relies on changes made to this file it will fail to work when
#  assessed.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used for generating the
# data set.
#

# Import standard Python functions for making "random" choices
from random import randint, choice

#
#--------------------------------------------------------------------#



#-----Data Set Function for Assessing Your Solution------------------#
#
# The function in this section is called by the assignment template
# to generate the data sets used by your program.

# The following function creates a random data set defining the
# overall image to draw.  Your program must work for ANY data set that
# can be produced by this function.  The results returned by calling
# this function will be used as the argument to your data visualisation
# function during marking.  For convenience during code development
# and marking this function also prints the data set generated to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
def raw_data():

    # Define the possible ways the object can move and turn
    moves = ['Move forward', 'Move & turn left', 'Move & turn right']
    # Define the possible initial orientations
    directions = ['North', 'North east', 'South east',
                  'South', 'South west', 'North west']

    # Choose the number of moves
    num_moves = randint(0, 10)
    # Choose the object's initial energy level
    # (which mustn't exceed the number of moves)
    energy = randint(0, num_moves)
    # Choose the object's initial orientation
    direction = choice(directions)

    # Keep track of how many moves have been created in total
    move_no = 0

    # Initialise the data set with the special first move
    random_moves = [[move_no, energy, direction]]

    # Create the remaining moves
    while move_no < num_moves:
        # Increment move number
        move_no = move_no + 1
        # Choose which way the object moves and turns
        move = choice(moves)
        # Add the new move to the data set
        random_moves.append([move_no, move])

    # Print the whole data set to the shell window, laid out
    # nicely, one move per line
    print("The moves to visualise are:\n")
    print(str(random_moves).replace('],', '],\n'))
    
    # Return the data set to the caller
    return random_moves

#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
# Some "fixed" data sets
#
# Developing code when the underlying data set changes randomly can
# be difficult.  To help you develop your code you can temporarily
# provide the call to the data generation function at the bottom of
# the assignment template file with a "seed" value which will force
# it to produce a known data set.  Of course, having completed your
# solution, your program must work for any list that can be returned
# by calling the data generation function with no argument.
#
# Some examples of useful seed numbers follow.  Of course, you are
# free to choose other seed values to help you debug your code.
#
# ---------
# Data sets where the object runs out of energy:
#
# 27864 - object faces north but has no energy and attempts
#         no moves
#
# 61889 - object faces south west but has no energy and
#         attempts no moves
#
# 89704 - object faces north west but has no energy and
#         doesn't move even though the data set has some
#         moves in it
#
# 87092 - object faces south west but has no energy and
#         doesn't move even though the data set has some
#         moves in it
#
# 68954 - object attempts only one move, ending in cell D6,
#         and is then exhausted
#
# 95296 - object only has energy for one move, ending up
#         exhausted in cell E3
#
# 13674 - object attempts only two moves, ending in cell D2,
#         and is then exhausted
#
# 90319 - object runs out of energy after two moves, ending
#         up exhausted in cell G5
#
# 37056 - object runs out of energy after three moves, ending
#         up exhausted in cell H4
#
# 78082 - object runs out of energy after three moves, ending
#         up exhausted in cell B4
#
# 71923 - literal "boundary case" where object runs out of energy
#         in top right corner, cell I9 (and doesn't leave the grid),
#         after 7 moves
#
# 22619 - boundary case where object runs out of energy
#         on right border, cell I7, after 5 moves (and
#         doesn't leave the grid)
#
# 43879 - boundary case where object runs out of energy
#         on right border, cell I7, after 4 moves (and
#         doesn't leave the grid)
#
# 78655 - object runs out of energy in cell A1
#
# 53007 - object is exhausted in cell G5 just before reaching
#         right-hand special cell
#
# ---------
# Data sets where the object moves outside the grid:
#
# 76312 - object goes straight out the top of the grid in its
#         third move
#
# 90944 - object goes straight out the bottom of the grid in
#         its third move
#
# 71185 - object exits bottom of grid in its third move (and
#         is last seen in cell D2)
#
# 20162 - object exits bottom of grid in its third move (and
#         is last seen in cell F2)
#
# 75629 - object exits bottom of grid in its fourth move (and
#         is last seen in cell C1)
#
# 79275 - object exits bottom of grid in its fourth move (and
#         is last seen in cell G1)
#
# 83665 - object exits bottom of grid in its fifth move (and
#         is last seen in cell H2)
#
# 15920 - object exits from left of grid in its fifth move
#         (last seen in cell A5)
#
# 6449 -  object exits from left of grid in its fifth move
#         (last seen in cell A5)
#
# 23011 - object exits at top of grid in its fifth move (and is
#         last seen in cell F8)
#
# 50190 - object exits at top of grid in its fourth move (and is
#         last seen in cell C9)
#
# 79199 - object exits at top of grid in its fourth move (and is
#         last seen in cell G9)
#
# 73841 - object exits at top of grid in its fifth move (and is
#         last seen in cell G9)
#
# 24013 - object exits at right of grid in its fifth move (and is
#         last seen in cell I5)
#
# ---------
# Data sets where the object reaches one of the special cells:
#
# 62112 - object finds the special cell on the right, H6, in three
#         moves
#         
# 82830 - object finds the special cell on the right in five
#         moves
#
# 60159 - object finds the special cell on the right in three
#         moves
#
# 53162 - object finds the top-left special cell, D8, in four moves
#
# 94510 - object finds the top-left special cell in two moves
#
# 7150  - object finds the top-left special cell in two moves
#
# 85582 - object finds the top-left special cell in two moves
#
# 99761 - object finds the bottom-left special cell, A3, in
#         four moves
#
# 61649 - object finds the bottom-left special cell in
#         four moves
#
# ---------
# Some long paths followed:
#
# 89444 - object almost walks a full circle but runs out of energy
#         in cell D2
#
# 7292  - object almost walks a perfect circle but makes a wrong
#         turn in the fifth step
#
# 22745 - object completes 8 moves but ends up exhausted in cell D2
#
# 26907 - object completes 8 moves but ends up exhausted in cell E7
#
#
#--------------------------------------------------------------------#

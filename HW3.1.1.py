# On my honor, as a CCSF student, I Keng Lum Aw have neither given or received
# inappropriate help with this assignment.
# Keng Lum Aw, October 30, 2018

##Design -- welcome the user to the world of clocks and prompt for yes or no. After
##that, prompt for positive or negative clock, then ask for displacement in the form
##of hh:mm.
##What I did was I first created functions for the turtle object and window, then
##a function for the hour hand and minute hand each. The last function I created was
##for verifying and converting displacement into integers.
##I started out with a welcome expression, a while loop asking for yes or no. Within
##the 'yes' response, I put another while loop asking for + or - clock. Then after
##that, I asked for the displacement. Lastly, the 'Once more?' code has the same
##structure as the beginning, but this code is within the while loop too.
##Within the + and - loop I add turtle graphics calling the functions to draw
##according to the response from the user.

import turtle
import time

def turtle_init(color, bgcolor, shape, size, speed):
    '''
    Create a window and turtle object that returns a tuple
    @params -- color, bgcolor, shape, size, speed
    @return tuple (terrapin, window)
    '''
    window = turtle.Screen()
    terrapin = turtle.Turtle()
    window.bgcolor(bgcolor)

    terrapin.color(color)
    terrapin.shape(shape)
    terrapin.speed(speed)
    terrapin.shapesize(size)
    return (terrapin, window)

def hr_hand(terrapin, time_, radius):
    '''
    Define a function for a turtle object to draw an hour hand
    @params -- turtle name(terrapin), time, the radius
    This functions calls for the turtle to move as written.
    '''
    hr_angle = ((time_*60 + hh_mm[1])*0.5)%360
    radius = radius
    terrapin.stamp()
    terrapin.right(hr_angle)
    terrapin.forward(radius)
    terrapin.shapesize(1)
    terrapin.stamp()
    terrapin.backward(radius)
    terrapin.left(hr_angle)
    terrapin.shape('blank')

def min_hand(terrapin, time_, radius):
    '''
    Define a function for a turtle object to draw minute hand given time,
    @params -- turtle object(terrapin), time, and the radius for the turtle
    to travel. 
    '''
    min_angle = (time_*6)%360
    terrapin.stamp()
    terrapin.right(min_angle)
    terrapin.forward(radius)
    terrapin.shape('arrow')
    terrapin.shapesize(1)
    terrapin.stamp()
    terrapin.backward(radius)
    terrapin.left(min_angle)
    terrapin.shape('blank')

def convert_int(s):
    '''
    Converts a string to an int if possible, and if not returns None:
    @param s -- input string
    @return, int or None 
    '''
    if len(s) >= 1 and s[0] == '-':
        # if s represents negative int
        if s[1:].isdigit():
            return int(s)
    elif s.isdigit():
        return int(s)
    else:
        return None # s doesn't return int
    
hh_mm = time.localtime()[3:5] # tuple class
hh_mm = list(hh_mm)  # now it's list class
                    

time_0 = [12,1,2,3,4,5,6,7,8,9,10,11]
time_1 = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]

print('Welcome to the time realization and displacement program!')
while True:
    test = input('Do you want to try it out [Y/N]? ') # Y/N response loop
    if test in 'Yy' and len(test) == 1:
        while True:
            test_1 = input('Do you see your world as negative or positive [-/+]? = ')
            if test_1 == '+':           # +/- response loop
                message_0 = input('The time is now. Your reaction to that bracing '\
                        'thought? ')   #add turtle graphics
                (bob, fatty) = turtle_init('black', 'white', 'arrow', 0.2, 20)
                bob.left(90)
                bob.penup()

                for time in time_0:
                    bob.forward(200)
                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                    bob.backward(200)
                    bob.right(30)

                (tom, fatty) = turtle_init('black', 'white', 'blank',0.2, 20)
                tom.left(90)
                tom.penup()
                tom.forward(225)
                tom.write(message_0,align = 'center',font=('Times New Roman',\
                                                                20,'normal'))
                bob.pendown()
                hr_hand(bob, hh_mm[0], 100)

                (ruth, fatty) = turtle_init('black', 'white', 'circle', 0.2, 20)
                ruth.left(90)
                
                min_hand(ruth, hh_mm[1], 160)
                while True:                         # displacement loop
                    displacement = input('Enter the time displacement in the format "hh:mm". '\
                                    'As examples, to go forward 2 hours and back 115 minutes, ' \
                                    'enter 2:-115; to go backward one hour exactly, enter -1:0.' \
                                    'Displacement: ').split(':')
                    if len(displacement) != 2:
                        print('The time displacement has to be in the format "hh:mm" only,'\
                        ' with numbers only, and cannot exceed two values, please try again.')
                        continue
                    elif len(displacement) == 2:
                        a = convert_int(displacement[0]) # call convert_int() function
                        b = convert_int(displacement[1])
                        if a == None or b == None:
                            print('The time displacement has to be either positive or negative '\
                                          'integer, please try again.')
                            continue
                        break
                fatty.resetscreen()
                (bob, fatty) = turtle_init('black', 'white', 'arrow', 0.2, 20)
                bob.left(90)
                bob.penup()

                for time in time_0:
                    bob.forward(200)
                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                    bob.backward(200)
                    bob.right(30)

                (tom, fatty) = turtle_init('black', 'white', 'blank',0.2, 20)
                tom.left(90)
                tom.penup()
                tom.forward(225)
                text = 'now' + ' + (' + str(a) + ':' + str(b) + ')'
                tom.write(text, align = 'center',font=('Times New Roman',20,'normal'))
                
                hr = (hh_mm[0] + a) % 12                # arithmetic to get time after displacement
                m = (hh_mm[1] + b) % 60
                hr += (hh_mm[1] + b) // 60
                hr %= 12
                bob.pendown()
                hr_hand(bob, hr, 100)

                (ruth, fatty) = turtle_init('black', 'white', 'circle', 0.2, 20)
                ruth.left(90)
                min_hand(ruth, m, 160)
                print(hh_mm, [hr,m])                    # displays current time followed by time after displacement
                while True:                             # 'Once more' while loop code
                    test = input('Once more [Y/N]? ')   # Y/N loop
                    import time
                    hh_mm = list(time.localtime()[3:5])
                    if test in 'Yy' and len(test) == 1:
                        while True:
                            test_1 = input('How do you rate your world this time, plus or minus [-/+]? = ')
                            if test_1 == '+':           # +/- loop
                                message_0 = input('The time is still now. Your reaction? ')   #add turtle graphics
                                fatty.resetscreen()
                                (bob, fatty) = turtle_init('black', 'white', 'arrow', 0.2, 20)
                                bob.left(90)
                                bob.penup()

                                for time in time_0:
                                    bob.forward(200)
                                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                                    bob.backward(200)
                                    bob.right(30)

                                (tom, fatty) = turtle_init('black', 'white', 'blank',0.2, 20)
                                tom.left(90)
                                tom.penup()
                                tom.forward(225)
                                tom.write(message_0,align = 'center',font=('Times New Roman',\
                                                                                20,'normal'))
                                bob.pendown()
                                hr_hand(bob, hh_mm[0], 100)

                                (ruth, fatty) = turtle_init('black', 'white', 'circle', 0.2, 20)
                                ruth.left(90)
                                min_hand(ruth, hh_mm[1], 160)
                                while True:             # displacement loop
                                    displacement = input('Enter the time displacement in the format "hh:mm". '\
                                                    'As examples, to go forward 2 hours and back 115 minutes, ' \
                                                    'enter 2:-115; to go backward one hour exactly, enter -1:0.' \
                                                    'Displacement: ').split(':')
                                    if len(displacement) != 2:
                                        print('The time displacement has to be in the format "hh:mm" only,'\
                                        ' with numbers only, and cannot exceed two values, please try again.')
                                        continue
                                    elif len(displacement) == 2:
                                        a = convert_int(displacement[0])
                                        b = convert_int(displacement[1])
                                        if a == None or b == None:
                                            print('The time displacement has to be either positive or negative '\
                                                          'integer, please try again.')
                                            continue
                                        break
                                fatty.resetscreen()
                                (bob, fatty) = turtle_init('black', 'white', 'arrow', 0.2, 20)
                                bob.left(90)
                                bob.penup()

                                for time in time_0:
                                    bob.forward(200)
                                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                                    bob.backward(200)
                                    bob.right(30)

                                (tom, fatty) = turtle_init('black', 'white', 'blank',0.2, 20)
                                tom.left(90)
                                tom.penup()
                                tom.forward(225)
                                text = 'now' + ' + (' + str(a) + ':' + str(b) + ')'
                                tom.write(text, align = 'center',font=('Times New Roman',20,'normal'))
                                
                                hr = (hh_mm[0] + a) % 12
                                m = (hh_mm[1] + b) % 60
                                hr += (hh_mm[1] + b) // 60
                                hr %= 12
                                bob.pendown()
                                hr_hand(bob, hr, 100)

                                (ruth, fatty) = turtle_init('black', 'white', 'circle', 0.2, 20)
                                ruth.left(90)
                                min_hand(ruth, m, 160)
                                print(hh_mm, [hr,m])
                                break
                            elif test_1 == '-':
                                message_0 = input('The time is still now. Your reaction? ')    #add negative turtle graphics
                                fatty.resetscreen()
                                (bob, fatty) = turtle_init('white', 'black', 'arrow', 0.2, 20)
                                bob.left(90)
                                bob.penup()

                                for time in time_1:
                                    bob.forward(200)
                                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                                    bob.backward(200)
                                    bob.right(30)

                                (tom, fatty) = turtle_init('white', 'black', 'blank',0.2, 20)
                                tom.left(90)
                                tom.penup()
                                tom.forward(225)
                                tom.write(message_0.swapcase()[::-1],align = 'center',font=('Times New Roman',\
                                                                                20,'normal'))
                                bob.pendown()
                                hr_hand(bob, hh_mm[0], 100)

                                (ruth, fatty) = turtle_init('white', 'black', 'circle', 0.2, 20)
                                ruth.left(90)
                                min_hand(ruth, hh_mm[1], 160)
                                while True:
                                    displacement = input('Enter the time displacement in the format "hh:mm". '\
                                                    'As examples, to go forward 2 hours and back 115 minutes, ' \
                                                    'enter 2:-115; to go backward one hour exactly, enter -1:0.' \
                                                    'Displacement: ').split(':')
                                    if len(displacement) != 2:
                                        print('The time displacement has to be in the format "hh:mm" only,'\
                                        ' with numbers only, and cannot exceed two values, please try again.')
                                        continue
                                    elif len(displacement) == 2:
                                        a = convert_int(displacement[0])
                                        b = convert_int(displacement[1])
                                        if a == None or b == None:
                                            print('The time displacement has to be either positive or negative '\
                                                          'integer, please try again.')
                                            continue
                                        break
                                fatty.resetscreen() 
                                (bob, fatty) = turtle_init('white', 'black', 'arrow', 0.2, 20)
                                bob.left(90)
                                bob.penup()

                                for time in time_1:
                                    bob.forward(200)
                                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                                    bob.backward(200)
                                    bob.right(30)

                                (tom, fatty) = turtle_init('white', 'black', 'blank',0.2, 20)
                                tom.left(90)
                                tom.penup()
                                tom.forward(225)
                                text = 'now' + ' + (' + str(a) + ':' + str(b) + ')'
                                tom.write(text, align = 'center',font=('Times New Roman',20,'normal'))
                                
                                hr = (hh_mm[0] + a) % 12
                                m = (hh_mm[1] + b) % 60
                                hr += (hh_mm[1] + b) // 60
                                hr %= 12
                                bob.pendown()
                                hr_hand(bob, hr, 100)

                                (ruth, fatty) = turtle_init('white', 'black', 'circle', 0.2, 20)
                                ruth.left(90)
                                min_hand(ruth, m, 160)
                                print(hh_mm, [hr,m])
                                break
                            else:
                                print('"' + test_1 + '"' + ' is not a valid response, please enter "+" '\
                                  'or "-".')
                    elif test in 'Nn' and len(test) == 1:
                        print('Goodbye from nows, thens, and futures! Have a nice day.')
                        break
                    else:
                        print('"' + test + '"' + ' is not a valid response, please enter "y" or "n".')   
            elif test_1 == '-':
                message_0 = input('The time is now. Your reaction to that bracing '\
                        'thought? ')    #add negative turtle graphics
                (bob, fatty) = turtle_init('white', 'black', 'arrow', 0.2, 20)
                bob.left(90)
                bob.penup()

                for time in time_1:
                    bob.forward(200)
                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                    bob.backward(200)
                    bob.right(30)

                (tom, fatty) = turtle_init('white', 'black', 'blank',0.2, 20)
                tom.left(90)
                tom.penup()
                tom.forward(225)
                tom.write(message_0.swapcase()[::-1],align = 'center',font=('Times New Roman',\
                                                                20,'normal'))
                bob.pendown()
                hr_hand(bob, hh_mm[0], 100)

                (ruth, fatty) = turtle_init('white', 'black', 'circle', 0.2, 20)
                ruth.left(90)
                min_hand(ruth, hh_mm[1], 160)
                while True:                     # displacement loop
                    displacement = input('Enter the time displacement in the format "hh:mm". '\
                                    'As examples, to go forward 2 hours and back 115 minutes, ' \
                                    'enter 2:-115; to go backward one hour exactly, enter -1:0.' \
                                    'Displacement: ').split(':')
                    if len(displacement) != 2:
                        print('The time displacement has to be in the format "hh:mm" only,'\
                        ' with numbers only, and cannot exceed two values, please try again.')
                        continue
                    elif len(displacement) == 2:
                        a = convert_int(displacement[0])
                        b = convert_int(displacement[1])
                        if a == None or b == None:
                            print('The time displacement has to be either positive or negative '\
                                          'integer, please try again.')
                            continue
                        break
                fatty.resetscreen() #window.bgcolor('black')
                (bob, fatty) = turtle_init('white', 'black', 'arrow', 0.2, 20)
                bob.left(90)
                bob.penup()

                for time in time_1:
                    bob.forward(200)
                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                    bob.backward(200)
                    bob.right(30)

                (tom, fatty) = turtle_init('white', 'black', 'blank',0.2, 20)
                tom.left(90)
                tom.penup()
                tom.forward(225)
                text = 'now' + ' + (' + str(a) + ':' + str(b) + ')'
                tom.write(text, align = 'center',font=('Times New Roman',20,'normal'))
                
                hr = (hh_mm[0] + a) % 12
                m = (hh_mm[1] + b) % 60
                hr += (hh_mm[1] + b) // 60
                hr %= 12
                bob.pendown()
                hr_hand(bob, hr, 100)

                (ruth, fatty) = turtle_init('white', 'black', 'circle', 0.2, 20)
                ruth.left(90)
                min_hand(ruth, m, 160)
                print(hh_mm, [hr,m])
                while True:
                    test = input('Once more [Y/N]? ') # 'Once more' loop
                    import time
                    hh_mm = list(time.localtime()[3:5])
                    if test in 'Yy' and len(test) == 1:
                        while True:
                            test_1 = input('How do you rate your world this time, plus or minus [-/+]? = ')
                            if test_1 == '+': 
                                message_0 = input('The time is still now. Your reaction? ')   #add turtle graphics
                                fatty.resetscreen()
                                (bob, fatty) = turtle_init('black', 'white', 'arrow', 0.2, 20)
                                bob.left(90)
                                bob.penup()

                                for time in time_0:
                                    bob.forward(200)
                                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                                    bob.backward(200)
                                    bob.right(30)

                                (tom, fatty) = turtle_init('black', 'white', 'blank',0.2, 20)
                                tom.left(90)
                                tom.penup()
                                tom.forward(225)
                                tom.write(message_0,align = 'center',font=('Times New Roman',\
                                                                                20,'normal'))
                                bob.pendown()
                                hr_hand(bob, hh_mm[0], 100)

                                (ruth, fatty) = turtle_init('black', 'white', 'circle', 0.2, 20)
                                ruth.left(90)
                                min_hand(ruth, hh_mm[1], 160)
                                while True:
                                    displacement = input('Enter the time displacement in the format "hh:mm". '\
                                                    'As examples, to go forward 2 hours and back 115 minutes, ' \
                                                    'enter 2:-115; to go backward one hour exactly, enter -1:0.' \
                                                    'Displacement: ').split(':')
                                    if len(displacement) != 2:
                                        print('The time displacement has to be in the format "hh:mm" only,'\
                                        ' with numbers only, and cannot exceed two values, please try again.')
                                        continue
                                    elif len(displacement) == 2:
                                        a = convert_int(displacement[0])
                                        b = convert_int(displacement[1])
                                        if a == None or b == None:
                                            print('The time displacement has to be either positive or negative '\
                                                          'integer, please try again.')
                                            continue
                                        break
                                fatty.resetscreen()
                                (bob, fatty) = turtle_init('black', 'white', 'arrow', 0.2, 20)
                                bob.left(90)
                                bob.penup()

                                for time in time_0:
                                    bob.forward(200)
                                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                                    bob.backward(200)
                                    bob.right(30)

                                (tom, fatty) = turtle_init('black', 'white', 'blank',0.2, 20)
                                tom.left(90)
                                tom.penup()
                                tom.forward(225)
                                text = 'now' + ' + (' + str(a) + ':' + str(b) + ')'
                                tom.write(text, align = 'center',font=('Times New Roman',20,'normal'))
                                
                                hr = (hh_mm[0] + a) % 12
                                m = (hh_mm[1] + b) % 60
                                hr += (hh_mm[1] + b) // 60
                                hr %= 12
                                bob.pendown()
                                hr_hand(bob, hr, 100)

                                (ruth, fatty) = turtle_init('black', 'white', 'circle', 0.2, 20)
                                ruth.left(90)
                                min_hand(ruth, m, 160)
                                print(hh_mm, [hr,m])
                                break
                            elif test_1 == '-':
                                message_0 = input('The time is still now. Your reaction? ')    #add negative turtle graphics
                                fatty.resetscreen()
                                (bob, fatty) = turtle_init('white', 'black', 'arrow', 0.2, 20)
                                bob.left(90)
                                bob.penup()

                                for time in time_1:
                                    bob.forward(200)
                                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                                    bob.backward(200)
                                    bob.right(30)

                                (tom, fatty) = turtle_init('white', 'black', 'blank',0.2, 20)
                                tom.left(90)
                                tom.penup()
                                tom.forward(225)
                                tom.write(message_0.swapcase()[::-1],align = 'center',font=('Times New Roman',\
                                                                                20,'normal'))
                                bob.pendown()
                                hr_hand(bob, hh_mm[0], 100)

                                (ruth, fatty) = turtle_init('white', 'black', 'circle', 0.2, 20)
                                ruth.left(90)
                                min_hand(ruth, hh_mm[1], 160)
                                while True:
                                    displacement = input('Enter the time displacement in the format "hh:mm". '\
                                                    'As examples, to go forward 2 hours and back 115 minutes, ' \
                                                    'enter 2:-115; to go backward one hour exactly, enter -1:0.' \
                                                    'Displacement: ').split(':')
                                    if len(displacement) != 2:
                                        print('The time displacement has to be in the format "hh:mm" only,'\
                                        ' with numbers only, and cannot exceed two values, please try again.')
                                        continue
                                    elif len(displacement) == 2:
                                        a = convert_int(displacement[0])
                                        b = convert_int(displacement[1])
                                        if a == None or b == None:
                                            print('The time displacement has to be either positive or negative '\
                                                          'integer, please try again.')
                                            continue
                                        break
                                fatty.resetscreen() #window.bgcolor('black')
                                (bob, fatty) = turtle_init('white', 'black', 'arrow', 0.2, 20)
                                bob.left(90)
                                bob.penup()

                                for time in time_1:
                                    bob.forward(200)
                                    bob.write(str(time),align = 'center',font=('Times New Roman',12,'normal'))
                                    bob.backward(200)
                                    bob.right(30)

                                (tom, fatty) = turtle_init('white', 'black', 'blank',0.2, 20)
                                tom.left(90)
                                tom.penup()
                                tom.forward(225)
                                text = 'now' + ' + (' + str(a) + ':' + str(b) + ')'
                                tom.write(text, align = 'center',font=('Times New Roman',20,'normal'))
                                
                                hr = (hh_mm[0] + a) % 12
                                m = (hh_mm[1] + b) % 60
                                hr += (hh_mm[1] + b) // 60
                                hr %= 12
                                bob.pendown()
                                hr_hand(bob, hr, 100)

                                (ruth, fatty) = turtle_init('white', 'black', 'circle', 0.2, 20)
                                ruth.left(90)
                                min_hand(ruth, m, 160)
                                print(hh_mm, [hr,m])
                                break
                            else:
                                print('"' + test_1 + '"' + ' is not a valid response, please enter "+" '\
                                  'or "-".')
                    elif test in 'Nn' and len(test) == 1:
                        print('Goodbye from nows, thens, and futures! Have a nice day.')
                        break
                    else:
                        print('"' + test + '"' + ' is not a valid response, please enter "y" or "n".')
            else:
                print('"' + test_1 + '"' + ' is not a valid response, please enter "+" '\
                  'or "-".')
                continue
            break
        break
    elif test in 'Nn' and len(test) == 1:
        print('Goodbye from nows, thens, and futures! Have a nice day.')
        break
    else:
        print('"' + test + '"' + ' is not a valid response, please enter "y" or "n".')

 
#13%12 == 1
#13%-12 == -11
#(13-7)%12 == 6
#(13-7)%-12 == -6

# Test Report
# After many tests, I have finally fixed everything that's wrong with my code to draw
# a clock and another one after the displacement.
# This is an example of the many times that I have tested my code out. 

# Welcome to the time realization and displacement program!
##Do you want to try it out [Y/N]? sa
##"sa" is not a valid response, please enter "y" or "n".
##Do you want to try it out [Y/N]? sd 34 
##"sd 34 " is not a valid response, please enter "y" or "n".
##Do you want to try it out [Y/N]? y
##Do you see your world as negative or positive [-/+]? = we
##"we" is not a valid response, please enter "+" or "-".
##Do you see your world as negative or positive [-/+]? = 30-+
##"30-+" is not a valid response, please enter "+" or "-".
##Do you see your world as negative or positive [-/+]? = +
##The time is now. Your reaction to that bracing thought? Test Positive
##Enter the time displacement in the format "hh:mm". As examples, to go forward 2 hours and back 115 minutes, enter 2:-115; to go backward one hour exactly, enter -1:0.Displacement: 30:-70
##[18, 48] [11, 38]
##Once more [Y/N]? er
##"er" is not a valid response, please enter "y" or "n".
##Once more [Y/N]? i
##"i" is not a valid response, please enter "y" or "n".
##Once more [Y/N]? y
##How do you rate your world this time, plus or minus [-/+]? = -
##The time is still now. Your reaction? EviTagen TSet
##Enter the time displacement in the format "hh:mm". As examples, to go forward 2 hours and back 115 minutes, enter 2:-115; to go backward one hour exactly, enter -1:0.Displacement: sa
##The time displacement has to be in the format "hh:mm" only, with numbers only, and cannot exceed two values, please try again.
##Enter the time displacement in the format "hh:mm". As examples, to go forward 2 hours and back 115 minutes, enter 2:-115; to go backward one hour exactly, enter -1:0.Displacement: 
##The time displacement has to be in the format "hh:mm" only, with numbers only, and cannot exceed two values, please try again.
##Enter the time displacement in the format "hh:mm". As examples, to go forward 2 hours and back 115 minutes, enter 2:-115; to go backward one hour exactly, enter -1:0.Displacement: 23:
##The time displacement has to be either positive or negative integer, please try again.
##Enter the time displacement in the format "hh:mm". As examples, to go forward 2 hours and back 115 minutes, enter 2:-115; to go backward one hour exactly, enter -1:0.Displacement: 30:-70
##[18, 53] [11, 43]
##Once more [Y/N]? we
##"we" is not a valid response, please enter "y" or "n".
##Once more [Y/N]? dsn
##"dsn" is not a valid response, please enter "y" or "n".
##Once more [Y/N]? 345
##"345" is not a valid response, please enter "y" or "n".
##Once more [Y/N]? 
##"" is not a valid response, please enter "y" or "n".
##Once more [Y/N]? n
##Goodbye from nows, thens, and futures! Have a nice day.
##>>> 

# Test 2
##Welcome to the time realization and displacement program!
##Do you want to try it out [Y/N]? we
##"we" is not a valid response, please enter "y" or "n".
##Do you want to try it out [Y/N]? d
##"d" is not a valid response, please enter "y" or "n".
##Do you want to try it out [Y/N]? n
##Goodbye from nows, thens, and futures! Have a nice day.
##>>>

# Test 3
##Welcome to the time realization and displacement program!
##Do you want to try it out [Y/N]? y
##Do you see your world as negative or positive [-/+]? = -
##The time is now. Your reaction to that bracing thought? 2 tseT
##Enter the time displacement in the format "hh:mm". As examples, to go forward 2 hours and back 115 minutes, enter 2:-115; to go backward one hour exactly, enter -1:0.Displacement: -45:65
##[18, 27] [10, 32]
##Once more [Y/N]? n
##Goodbye from nows, thens, and futures! Have a nice day.
##>>> 




# Hacking Version 4
# This is a graphical password guessing game that displays a 
# list of potential computer passwords. The player is allowed 
# 1 attempt to guess the password. The game indicates that the 
# player failed to guess the password correctly if guessed incorrectly
# and succeeded to enter if guessed correctly.

from uagame import Window
from time import sleep

# create window
window = Window('Hacking', 600, 500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

line_height =  window.get_font_height()
SLEEP_TIME = 0.3
Line_Y = 0
header = ['DEBUG MODE','1 ATTEMPT(S) LEFT','']

# display header
for header_line in header:
    window.draw_string(header_line, 0, Line_Y)
    window.update()
    sleep(SLEEP_TIME)
    Line_Y = Line_Y + line_height

# display password list

password_list= ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE'
                , 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING'
                , 'PUTTING']
for password_line in password_list:
    window.draw_string(password_line, 0, Line_Y)
    window.update()
    sleep(SLEEP_TIME)
    Line_Y = Line_Y + line_height

# prompt for guess
guess = window.draw_string('',0 , Line_Y)
window.update()
sleep(1)
Line_Y = Line_Y + line_height

guess = window.input_string('ENTER PASSWORD >',0 , Line_Y)
window.clear()
Line_Y = Line_Y + line_height

# create outcome
#    success outcome
if guess == 'HUNTING':
    outcome = [guess, '', 'EXITING DEBUG MODE', ''
               , 'LOGIN SUCCESSFUL - WELCOME BACK', ''
               , 'PRESS ENTER TO CONTINUE']
        
#    failure outcome
else:
    outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', ''
               , 'PLEASE CONTACT AN ADMINISTRATOR',''
               , 'PRESS ENTER TO EXIT'] 

# end game


width = window.get_width()
height = window.get_height()
#   display guess

num = -3.5

for outcome_line in outcome[0:6]:
    string_width = window.get_string_width(outcome_line)
    window.draw_string(outcome_line, (width-string_width)//2 , (height//2 + int(line_height*num)))    
    window.update()
    sleep(SLEEP_TIME)
    num = num + 1
#   displayer prompt for end
string_width = window.get_string_width(outcome[6])
window.input_string(outcome[6],(width-string_width)//2 ,(height//2 + int(line_height*num)))
window.close()
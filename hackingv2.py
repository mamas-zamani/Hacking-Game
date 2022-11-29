# Hacking Version 2
# This is a graphical password guessing game that displays a 
# list of potential computer passwords. The player is allowed 
# 1 attempt to guess the password. The game indicates that the 
# player failed to guess the password correctly.

from uagame import Window
from time import sleep

# create window
window = Window('Hacking', 600, 500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

line_height =  window.get_font_height()

# display header
window.draw_string('DEBUG MODE', 0, 0)
window.update()
sleep(0.3)

window.draw_string('1 ATTEMPT(S) LEFT', 0, 1*line_height)
window.update()
sleep(0.3)

window.draw_string('', 0, 2*line_height)
window.update()
sleep(0.3)

# display password list

window.draw_string('PROVIDE', 0, 3*line_height)
window.update()
sleep(0.3)
window.draw_string('SETTING', 0, 4*line_height)
window.update()
sleep(0.3)
window.draw_string('CANTINA', 0, 5*line_height)
window.update()
sleep(0.3)
window.draw_string('CUTTING', 0, 6*line_height)
window.update()
sleep(0.3)
window.draw_string('HUNTERS', 0, 7*line_height)
window.update()
sleep(0.3)
window.draw_string('SURVIVE', 0, 8*line_height)
window.update()
sleep(0.3)
window.draw_string('HEARING', 0, 9*line_height)
window.update()
sleep(0.3)
window.draw_string('HUNTING', 0, 10*line_height)
window.update()
sleep(0.3)
window.draw_string('REALIZE', 0, 11*line_height)
window.update()
sleep(0.3)
window.draw_string('NOTHING', 0, 12*line_height)
window.update()
sleep(0.3)
window.draw_string('OVERLAP', 0, 13*line_height)
window.update()
sleep(0.3)
window.draw_string('FINDING', 0, 14*line_height)
window.update()
sleep(0.3)
window.draw_string('PUTTING', 0, 15*line_height)
window.update()
sleep(0.3)

# prompt for guess
guess = window.draw_string('',0 , 16*line_height)
window.update()
sleep(1)

guess = window.input_string('ENTER PASSWORD >',0 , 17*line_height)
window.clear()              


# end game


width = window.get_width()
height = window.get_height()
#   display guess

string_width = window.get_string_width(guess)
window.draw_string(guess, (width-string_width)//2 , (height//2 - int(line_height*3.5)))    
window.update()
sleep(0.3)

window.draw_string('',0 , (height//2 - int(line_height*2.5)))    
window.update()
sleep(0.3)
#   display failure outcome line 1

string_width = window.get_string_width('LOGIN FAILURE - TERMINAL LOCKED')
window.draw_string('LOGIN FAILURE - TERMINAL LOCKED',(width-string_width)//2 ,(height//2 - int(line_height*1.5))) 
window.update()
sleep(0.3)

window.draw_string('',0 , (height//2 - int(line_height*0.5)))    
window.update()
sleep(0.3)
#   display failutre outcome line 2

string_width = window.get_string_width('PLEASE CONTACT AN ADMINISTRATOR')
window.draw_string('PLEASE CONTACT AN ADMINISTRATOR',(width-string_width)//2 ,(height//2 + int(line_height*0.5))) 
window.update()
sleep(0.3)

window.draw_string('',0 , (height//2 + int(line_height*1.5)))    
window.update()
sleep(0.3)
#   displayer prompt for end
string_width = window.get_string_width('PRESS ENTER TO EXIT')
window.input_string('PRESS ENTER TO EXIT',(width-string_width)//2 ,(height//2 + int(line_height*2.5)))
window.close()
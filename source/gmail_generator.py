#! python3

#   Author      : Stavros Grigoriou
#   Updated    : yungK1LL
#   GitHub      : https://github.com/unix121
#   GitHub      : https://github.com/blooditrix
#   Year        : 2018
#   Description : [Updated]Script that generates random Gmail account. Still stalls at phone verification.

import pyautogui
import sys
import time
import random
import string

# Printing funtion with 3 modes
# 1 : Normal message
# 2 : Information message
# 3 : Caution message
def msg(
        _option_,
        _message_
        ):
    if _option_ == 1:
        print('\x1b[0;32;40m> %s\x1b[0m' % _message_)
    elif _option_ == 2:
        print('\x1b[0;32;40m>\x1b[0m %s' % _message_)
    elif _option_ == 3:
        print('\n\x1b[0;32;40m[\x1b[0m%s\x1b[0;32;40m]\x1b[0m' % _message_)
    else:
        print('\n\x1b[0;31;40m[ERROR]\x1b[0m')

# Exiting function
def ext():
    msg(1,'Exiting...')
    sys.exit()


# Function used to open Firefox
def open_firefox():

    # Printing basic message
    msg(1,'Opening Firefox...')

    # Location the start button
    _start_button_=pyautogui.locateOnScreen('images/start_button.png')
    _location_=pyautogui.center(_start_button_)

    # Clicking the start button
    if not  pyautogui.click(_location_):
        msg(1,'¡El menú de inicio se abrió correctamente!')
    else:
        msg(3,'¡Error al abrir el menú de inicio!')
        ext()

    time.sleep(2)

    # Search for Firefox in the menu search
    pyautogui.typewrite('firefox')
    pyautogui.typewrite('\n')
    
    # Print message
    msg(1,'Firefox ahora está abierta y en ejecución.')


# Function used to locate GMail
def locate_gmail():
    
    #Sleep for a while and wait for Firefox to open
    time.sleep(3)

    # Printing message
    msg(1,'Abriendo Gmail...')

    # Typing the website on the browser
    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft')
    pyautogui.typewrite('https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default')
    pyautogui.typewrite('\n')
    
    # Wait for a while until the website responds
    time.sleep(6)

    # Print a simple message
    msg(1,'Localizando el formulario...')

    # Locate the form
    pyautogui.press('tab')
 
    time.sleep(2)

    _gmail_ = pyautogui.locateOnScreen('images/gmail_form.png')
    formx, formy = pyautogui.center(_gmail_)
    pyautogui.click(formx, formy)
    
    # Check and print message
    if not pyautogui.click(formx, formy):
        msg(1,'Ubicado el formulario.')
    else:
        msg(3,'No se pudo localizar el formulario.')
        ext()


# Function used to randomize credentials
def randomize(
                _option_,
                _length_
            ):

    if _length_ > 0 :

        # Options:
        #       -p      for letters, numbers and symbols
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-l':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_='1234567890'
        elif _option_ == '-m':
            string._characters_='JFMASOND'

        if _option_ == '-d':
            _generated_info_=random.randint(1,28)
        elif _option_ == '-y':
            _generated_info_=random.randint(1950,2000)
        else:
            _generated_info_=''
            for _counter_ in range(0,_length_) :
                _generated_info_= _generated_info_ + random.choice(string._characters_)

        return _generated_info_

    else:
        msg(3,'No se especificó ninguna longitud válida...')
        ext()


# Function used to generate the credential information
def generate_info():

    # Print message
    msg(1,'Generando credenciales...')

    # First and last name
    _first_name_=randomize('-l',7)
    pyautogui.typewrite(_first_name_)
    pyautogui.typewrite('\t')
    _last_name_=randomize('-l',8)
    pyautogui.typewrite(_last_name_)
    pyautogui.typewrite('\t')
    msg(2,'\x1b[0;33;40mNombre:\x1b[0m %s %s' % (_first_name_,_last_name_))

    # Username
    _username_=randomize('-l',10)
    pyautogui.typewrite(_username_)
    pyautogui.typewrite('\t')
    msg(2,'\x1b[0;33;40mNombre de usuario:\x1b[0m %s' % _username_)

    # Password
    _password_=randomize('-p',16)
    pyautogui.typewrite(_password_+'\t'+_password_+'\t')
    msg(2,'\x1b[0;33;40mPassword:\x1b[0m %s' % _password_)

    # Date of birth
    _month_=randomize('-m',1)
    _day_=randomize('-d',1)
    _year_=randomize('-y',1)
    pyautogui.typewrite(_month_+'\t'+str(_day_)+'\t'+str(_year_)+'\t')
    msg(2,'\x1b[0;33;40mFecha de nacimiento:\x1b[0m %s/%d/%d' % (_month_,_day_,_year_))

    # Gender (set to 'Rather not say')
    pyautogui.typewrite('R\t')
    msg(2,'\x1b[0;33;40mGénero:\x1b[0m Prefiero no decirlo')

    # Skip the rest
    pyautogui.typewrite('\t\t\t\t\n')

# Main function
if __name__=='__main__':

    if open_firefox() :
        msg(3,'No se pudo ejecutar el comando "abrir firefox".')
        ext()

    if locate_gmail() :
        msg(3,'No se pudo ejecutar el comando "locate_gmail".')
        ext()

    if generate_info() :
        msg(3,'No se pudo ejecutar el comando "generate_info".')
        ext()

    msg(1,'Hecho...')
    ext()

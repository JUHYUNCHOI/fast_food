import streamlit as st
import os
import time
import random
from pygame import mixer
from PIL import Image
import time

def getImage(image):
    current_file = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(current_file, '..', 'resources', 'upAndDown', image)

def getSound(file):
    current_file = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(current_file, '..', 'resources', 'upAndDown', file)

def up(component):
    image = Image.open(getImage('up.PNG'))
    component.image(image, caption='Up입니다.')
    bigger_voice = getSound('bigger.mp3')

    mixer.init()  # Initialzing pyamge mixer

    mixer.music.load(bigger_voice)
    mixer.music.play()

    # time.sleep(5)
    #
    # mixer.music.stop()

def down(component):
    image = Image.open(getImage('down.PNG'))
    component.image(image, caption='Down입니다.')
    smaller_voice = getSound('smaller.mp3')

    mixer.init()  # Initialzing pyamge mixer

    mixer.music.load(smaller_voice)
    mixer.music.play()

def correct(component):
    image = Image.open(getImage('correct.jpg'))
    component.image(image, caption='정답입니다.')
    correct_voice = getSound('correct.mp3')

    mixer.init()  # Initialzing pyamge mixer

    mixer.music.load(correct_voice)
    mixer.music.play()


def setRandomNumber():
    st.session_state['randomNumber'] = random.randint(1, 10)

def getRandomNumber():
    if 'randomNumber' in st.session_state:
        return st.session_state['randomNumber']

def clearRandomNumber():
    st.write('clearRandomNumber')
    st.session_state.pop('randomNumber')
    st.write(st.session_state)

def clearPlayerNumber():
    st.session_state['playerNumber'] = ''

def isSubmitDisabled():
    ss = st.session_state
    if 'isSubmitDisabled' in ss and ss['isSubmitDisabled'] == '':
        return True
    return False

def drawUpAndDownGamePage():
    game = st.container()

    header = game.container()
    body = game.container()
    footer = game.container()
    header.title('Up and Down')
    start_button = header.button('게임시작')

    if start_button:
        setRandomNumber()
        clearPlayerNumber()

    computer = getRandomNumber()
    st.write(computer)
    if computer != None:
        input = body.text_input('숫자를 입력하세요: ', key='playerNumber')
        input = input.strip()
        if input != '':
            input = int(input)

        submit = body.button('제출', disabled=isSubmitDisabled())
        if submit or input:
            if input > computer:
                down(footer)
            elif input < computer:
                up(footer)
            else:
                correct(footer)
                time.sleep(3)
                clearRandomNumber()


if __name__ == "__main__":
    drawUpAndDownGamePage()
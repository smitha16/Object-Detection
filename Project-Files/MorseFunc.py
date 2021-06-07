
import winsound
import time

def MorseGen(inLet):
    #inLet = 'z'
    MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..'
                    }
    
    code = MORSE_CODE_DICT[inLet]
    
    for i in code:
        if i == '.':
            winsound.Beep(500,100)
            
        else :
            winsound.Beep(500,300)
        
        time.sleep(0.2)
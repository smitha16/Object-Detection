import winsound
import time
def TernOut(inNum):
    
    code =''
    if inNum == 1 :
        code = '0'
    else :
        while(inNum > 0):
            code += str(inNum%3)
            inNum = int(inNum/3)
    code =''.join(reversed(code))
    
    winsound.Beep(500,100)
    time.sleep(0.5)
    for i in code :
        if(i=='0'):
            winsound.Beep(500,100)
        if(i=='1'):
            winsound.Beep(500,500)
        if(i=='2'):
            winsound.Beep(1000,300)
        time.sleep(0.2)

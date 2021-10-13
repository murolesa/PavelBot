from time import sleep
from random import randint
import pyautogui
import pytesseract

#pytessetact config:
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
config = r'--oem 3 --psm 6'

with open('messages.txt') as file:
    messages = file.readlines()

end = len(messages) - 1
x = randint(0, end)

def name_find_and_send_message(name, message_to_send):
    screenshot = pyautogui.screenshot(region=(900, 838, 720, 100))
    message = pytesseract.image_to_string(screenshot, config=config)
    
    sleep(5)
    if name in message:
        pyautogui.moveTo(1090, 969)
        pyautogui.doubleClick()
        pyautogui.hotkey('shift', 'alt')    #Переключаю раскладку, чтобы печатало русскими буквами.
        pyautogui.write(message_to_send)
        sleep(1)
        pyautogui.press('enter')
        pyautogui.hotkey('shift', 'alt')    #Переключает расскладку обратно
        print(x)
        print(messages[x])
    else:
        # pass
        print('Нет Паши')
        # break

try:
    while True:
        name_find_and_send_message('Pavel Veshnyagov', messages[x])   #Gfif? blb yf[eq! = иди нахуй
        
except KeyboardInterrupt:
    print('Stopping work of bot..')

    

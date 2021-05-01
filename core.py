import datetime
from text_to_speech import speak
from speech_to_text import takeCommand
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyautogui
import requests
import wolframalpha


wolframalpha_app_id = "T4YK7T-V57PLRVP6L"

# Simple features

def time_():
    # Get current time 
    time = datetime.datetime.now().strftime("%H:%M") # For 24 hour clock
    speak(f"Bây giờ là {time}")


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    if month == 4:
        month = "tư"
    speak(f"Hôm nay là ngày {day} tháng {month} năm {year}")

def wiki(text):
    wikipedia.set_lang("vi")
    result = wikipedia.summary(text, sentences=3)
    speak(f"Theo wikipedia {result}")

def sendEmail(to, content):
    sever = smtplib.SMTP("smtp.gmail.com", 587)
    sever.ehlo()
    sever.starttls()
    sever.login("nvkha96@gmail.com", "")
    sever.sendmail("nvkha96@gmail.com", to, content)
    sever.close()


def bowser(query):
    chromepath = "C:\\Program Files\\Google\\Chrome\\Application"
    wb.get(chromepath).open_new_tab(query+'.com')

def youtube():
    speak("Bạn muốn tìm gì trên youtube")
    query = takeCommand().lower()
    wb.open(f"https://www.youtube.com/results?search_query={query}")

def cpu():
    usage = str(psutil.cpu_percent())
    ram = str(psutil.virtual_memory().percent)
    battery = str(psutil.sensors_battery().percent)
    speak(f"CPU máy tính của bạn đang sử dụng {usage}%")
    speak(f"Bạn đang sử dụng {ram}% ram")
    speak(f"Máy tính của bạn còn lại {battery}% pin")
    
def writeNote():
    speak("Bạn muốn nội dung là gì")
    notes = takeCommand()
    file = open('note.txt', 'w', encoding="utf-8") 
    file.write(notes)
    file.close()
    speak("Ghi chú của bạn đã được lưu")

def openNote():
    file = open('note.txt', 'r', encoding="utf-8")
    speak("Ghi chú của bạn có nội dung là")
    speak(file.read())


def screenshot():
    img = pyautogui.screenshot()
    img.save('screenshot.png')
    speak("Màn hình đã được chụp")


# Remember info from user 
def remember():
    speak("Bạn muốn tôi ghi nhớ gì nào")
    memory = takeCommand()
    with open("memory.txt", "w", encoding="utf-8") as file:
        file.write(memory)

# Advanced features 
    
def get_news():
    speak("Cho tôi biết chủ đề bạn muốn tôi cập nhật nhé")
    article = takeCommand()
    url = f"https://gnewsapi.net/api/search?q={article}&country=vn&language=vi&limit=5&api_token=SMgqw4DJVDARezeA5zkbVPEos9JrDcELRmBp7RVwhwzYGDrUx46GuqmRtIvr"

    payload = "\n"
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    for news in response['articles']:
        speak(news['title'])
        print(news['article_url'])

def calculate():
    query = "tính 121323 + 65767"
    client = wolframalpha.Client(wolframalpha_app_id)
    index = query.lower().split().index("tính")
    query = query.split()[index + 1:]
    res = client.query(''.join(query))
    answer = next(res.results).text
    print(''.join(query) + "=" + answer)
    speak(''.join(query) + "=" + answer)
    

calculate()

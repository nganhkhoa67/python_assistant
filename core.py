import datetime
from text_to_speech import speak
import wikipedia
import smtplib
import webbrowser as wb
import psutil

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

def youtube(query):
    wb.open(f"https://www.youtube.com/results?search_query={query}")

def cpu():
    usage = str(psutil.cpu_percent())
    ram = str(psutil.virtual_memory().percent)
    battery = str(psutil.sensors_battery().percent)
    speak(f"CPU máy tính của bạn đang sử dụng {usage}%")
    speak(f"Bạn đang sử dụng {ram}% ram")
    speak(f"Máy tính của bạn còn lại {battery}% pin")
    
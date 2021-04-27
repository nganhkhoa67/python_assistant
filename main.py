from text_to_speech import speak
from speech_to_text import takeCommand

import datetime

# Get input from user 
# input = takeCommand()

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

date_()


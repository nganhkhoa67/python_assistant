from text_to_speech import speak
from speech_to_text import takeCommand
import core


if __name__ == "__main__":
    while True:
        # Get input from user 
        query = takeCommand().lower()

        if "mấy giờ" in query:
            core.time_()
        elif "ngày mấy" in query:
            core.date_()
        elif "tìm wikipedia" in query:
            core.wiki(query)
        elif 'youtube' in query:
            speak("Bạn muốn tìm gì trên youtube")
            search_query = takeCommand().lower()
            core.youtube(search_query)
        elif "tình trạng máy tính" in query:
            core.cpu()
            


        







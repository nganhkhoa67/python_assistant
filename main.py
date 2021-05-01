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
            core.youtube()
        elif "tình trạng máy tính" in query:
            core.cpu()
        elif "bye" in query:
            speak("Hẹn gặp lại bạn sau")
            quit()
        elif "viết ghi chú" in query:
            core.writeNote()
        elif "mở ghi chú" in query:
            core.openNote()
        elif "chụp màn hình" in query:
            core.screenshot()
        elif "ghi nhớ" in query:
            core.remember()
            
            


        







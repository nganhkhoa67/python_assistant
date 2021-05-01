from playsound import playsound
import os
import json
import requests



# Convert text to speak
def speak(text=''):
    url = "https://viettelgroup.ai/voice/api/tts/v1/rest/syn"
    data = {"text": text, "voice": "doanngocle", "id": "2", "without_filter": False, "speed": 1.0, "tts_return_option": 3}
    headers = {'Content-type': 'application/json', 'token': 'WAMmL2k7yuyc0-Jl2RZkTxQxtFtwHbVdldPHYhiNJsKCVemaSdrxuMGrRcI7FOKE'}

    #if encounter SSL error because of https certificate, please comment out above line and use the line below to  make insecure connections   (this will expose your application to security risks, such as man-in-the-middle attacks.)
    response = requests.post(url, data=json.dumps(data), headers=headers)
    data = response.content
    f = open("output.mp3", "wb")
    f.write(data)
    f.close()
    playsound("output.mp3") 
    os.remove("output.mp3")

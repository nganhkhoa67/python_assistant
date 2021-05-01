from neuralintents import GenericAssistant
from googletrans import Translator

translator = Translator()

assistant = GenericAssistant('intents.json', model_name="test_model")
assistant.train_model()
assistant.save_model()

done = False

while not done:
    message = input("Enter a message: ")
    message = translation = translator.translate(message, dest='en')
    if message == "STOP":
        done = True
    else:
        assistant.request(message.text)
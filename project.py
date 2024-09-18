import speech_recognition as sr
import pyttsx3 as t
import webbrowser as wb

engine=t.init()

def speak(a):
    engine.say(a)
    engine.runAndWait()
    print(a)

def processcommand(c):
    if("open google" in c.lower()):
        speak("opening google")
        wb.open("https://google.com")

    elif("open youtube" in c.lower()):
        speak("opening youtube")
        wb.open("http://youtube.com")

    elif("open gmail" in c.lower()):
        speak("opening gmail")
        wb.open("https://g.co/kgs/4phxcA8")
    
    elif("open chat gpt" in c.lower()):
        speak("opening chat GPT")
        wb.open("https://chatgpt.com/")

    elif("exit" in c.lower()):
        speak("python shutting down")
        exit()  

    else:
        pass
        

        try:
            with sr.Microphone() as source:
                print("Python is listening to your command...")
                audio = r.listen(source)
            request=r.recognize_google(audio)
            print(request)
            processcommand(request)
            

        except sr.UnknownValueError:
            print("Could you please speak a little louder please")
        
    


while True:
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Python is listening...")
            audio = r.listen(source)
        word=r.recognize_google(audio)

        if("python" in word.lower()):
            try:
                with sr.Microphone() as source:
                    speak("What would you like to do sir?")
                    print("Python is listening to your command...")
                    audio = r.listen(source)
                request=r.recognize_google(audio)
        
                processcommand(request)
            

            except sr.UnknownValueError:
                print("Could you please speak a little louder please")

            

    except sr.UnknownValueError:
        print("Could you please speak a little louder please")
    
    




   
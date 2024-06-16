# Female Replacement Intelligent Digital Assistant Youth(F.R.I.D.A.Y)






import pyttsx3
import datetime
import wikipedia
import webbrowser




# for taking microphone input form user
import speech_recognition as sr



engine = pyttsx3.init('sapi5')
# use inbuilt voices
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty('voice',voices[2].id)


def speak(audio):
    # it will speak what argument(audio) is given
    engine.say(audio)
    engine.runAndWait()
    
# first import datetime hour
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning PARMESHWAR WAKDE ")
    elif hour>=12 and hour < 18:
        speak("Good afternoon PARMEHWAR WAKDE ")
    else :
        speak("Good Evening PARMESHWAR WAKDE")
    speak("Welcome aboard! I'm Friday, your virtual companion. Think of me as your tech-savvy wingman, ready to assist you in navigating the digital cosmos with style and flair.")                
    
def takeCommand():
    # it Takes microphone input from user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening............")
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        
        
        print("say that again  please....")
        return "None"    
    
    return query
    
if __name__ == "__main__":
    wishme() #wish command should be in starting only
    while True:  
        query = takeCommand().lower() #convert the query in lowercase
        
        if 'exit' in query or 'stop' in query or 'quit' in query:
            print("Exiting Program......")
            speak("Sure, I'll stop now.")
            break  
        # Logic for executing task
        elif 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2) #speak 2 sentences from wikipedia
            speak("According  to Wikipedia")
            speak(results)
            print(results)
        
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")   
        elif "open google chrome" in query:
            webbrowser.open("https://www.google.com/") 
        elif "open gmail" in  query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            
        
        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime(" %H:%M:%S")  #specifer for time(day,month...)  
            speak(f"Sir,the time is {strTime}")
            
        elif "what is today's date " in query:
            strTime = datetime.datetime.now().strftime("%d/%m/%Y")  #specifer for time(day,month...)  
            speak(f"Sir,the date is {strTime}")
                
            
            
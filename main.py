'''
pyttsx3 >> python text to speech.
speech_recognition >> used to convert spoken words to text and works on API's.
automate_wikipedia >> used to automate and work with the wikipedia.
webbrowser >> used for to automate webbrowsers.
smtplib >> sending emails.
os >> used to work/ interact with operating system.
datetime >> used to work with date and time.
'''

# to install the libraries type
import datetime
import os
import smtplib
import webbrowser
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip get install speechRecognition
import wikipedia  # pip install wikipedia

engine = pyttsx3.init('sapi5')  # driver or voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)  # perticular time right now
    # 12:00 - noon/ midnight  1:00 - morning/ afternoon it can't recognize the am and pm
    # 18:00 - evening
    if 0 <= hour <= 12:
        speak("Good Morning sir")
    elif 12 <= hour <= 18:
        speak("Good Afternoon sir")
    else:
        speak("Good evening Sir")
    speak(" Let me know how can I help you ? What are you looking for ?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you sir.......")
        r.pause_thresold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your voice......")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir you said: {query}\n")

    except Exception as e:
        print("Sir say that again please......")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("............", "..............")   #  sender's email id and password in respective blank places
    server.sendmail("..............", to, content)   # sender's email id
    server.close()




if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()


                #less secure app access should on in your default browser to automate work on browser

        if "open wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentence=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


                  # file location path in the respective blank spaces

        if "word" in query:
            npath = "................................."
            os.startfile(npath)

        elif "excel" in query:
            npath = "................................."
            os.startfile(npath)

        elif "powerpoint" in query:
            npath ="..................................."
            os.startfile(npath)

        elif "by" in query:
            speak("Bye sir, see you soon")

        elif "good night" in query:
            speak("good night sir")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "tell me the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")


                    # URL link should be in the blank space

        elif "open my youtube channel" in query:
            webbrowser.open("................................")


                   # less secure app access should on in your default browser to automate work on browser

        elif "send email" in query:
            try:
                speak("what should I send sir?")
                content = takecommand()
                to = "......................"     # reciver's email id should be in the blank place
                sendEmail(to, content)
                speak("sir, your email has been sent successfully")

            except Exception as e:
                print(e)
                speak("sir I am unable to send to email please address the error")

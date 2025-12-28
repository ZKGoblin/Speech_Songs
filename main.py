import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

r.energy_threshold = 300          
r.dynamic_energy_threshold = False

def record_text():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, phrase_time_limit=5)

            # Recognise speech
            text = r.recognize_google(audio, language="en-GB")
            print("Recognised:", text)
            return text

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print("Could not understand audio")

    return None

def output_text(text):
    if text is None:
        return

    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

with sr.Microphone() as source:
    print("Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Calibration complete.")

while True:
    text = record_text()
    output_text(text)
    print("Wrote text\n")

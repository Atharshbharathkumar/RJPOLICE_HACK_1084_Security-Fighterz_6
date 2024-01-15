import speech_recognition as sr
import webbrowser
import pyautogui 

def process_command(command):
    if "open notepad" in command:
        pyautogui.hotkey('winleft', 'r')
        pyautogui.write('notepad')
        pyautogui.press('enter')
    elif "close notepad" in command:
        pyautogui.hotkey('alt', 'f4')
    elif "open case file" in command:
        webbrowser.open('Case_file.html')

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()
                print("You said:", command)
                process_command(command)
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()

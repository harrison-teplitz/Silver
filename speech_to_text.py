import speech_recognition as sr

def convert_wav_to_text(file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(f"{file}") as source:
        audio_data = recognizer.record(source)  # Read the entire audio file

    # Recognize the speech in the audio file
    try:
        text = recognizer.recognize_google(audio_data)
        #print("Transcription: ", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

#for testing
#print(convert_wav_to_text("Beth_audio_files/Beth_role_models.wav"))
        
import time
import os

def run_into(sleep):
    print("begin cloning process...")
    if sleep:
        time.sleep(1)
    print("I am going to ask you some questions and will build a clone of yourself")
    if sleep:
        time.sleep(3)
    print("for your loved ones to talk to for many years.")
    if sleep:
        time.sleep(4) 
    print("When you are presented with a question press enter/return to begin the recording")
    if sleep:
        time.sleep(4)
    print("when you have completed your response, press enter/return to finish the recording")
    if sleep:
        time.sleep(3)
    print("Are you ready to begin? (press any enter/return to continue?)")
    input()

def get_name():
    print("First thing first, what is your name?")
    name = input()
    return name

def get_descriptor(name):
    print(f"Thank you {name}, and how would you describe yourself; gender, occupation, age?")
    descriptor = input()
    return descriptor

def create_audio_directory(name):
    directory_name = f"{name}_audio_files"
    try:
        os.makedirs(directory_name, exist_ok=True)  # exist_ok=True avoids raising an error if the directory already exists
        print(f"Directory '{directory_name}' created successfully.")
    except OSError as error:
        print(f"Error creating directory '{directory_name}': {error}")  
    return directory_name


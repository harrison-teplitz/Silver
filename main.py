from clone_voice import *
from record_audio import get_recording
from speech_to_text import convert_wav_to_text
from chat import *
from misc import *
import questions
import json
import time

def build_clone():
        run_into(sleep = False)
        name = get_name()
        description = get_descriptor(name)
        print(f"Thank you {name}, let's begin")
        directory = create_audio_directory(name)
        q_count = 1
        responses = {}

        for question_name, question in questions.questions.items():
            print(f"Question #{q_count}:")
            print(question)
            print("press enter/return to begin your response")
            input()
            get_recording(name,question_name,directory)
            print("processing response...")
            responses[question_name] = convert_wav_to_text(f"{directory}/{name}_{question_name}.wav")
            user_input = input("Do you want to continue? (yes/no): ").strip().lower()
            if user_input == 'no':
                break
        
        with open(f"{name}_context.json", 'w') as json_file:
            json.dump({"description":description,"responses":responses}, json_file)
        
        

        with open(f"{name}_context.json", 'r') as json_file:
            loaded_data = json.load(json_file)

        #print(loaded_data)
        add_voice(name, description, directory)

def converse(name):
    voice_id = voice_id_search(name)
    with open(f"{name}_context.json", 'r') as json_file:
            initial_context = json.load(json_file)
    context = [{"role": "system", "content": f'Your name is {name} and\
             these are your basic attributes: {initial_context["description"]}.\
             Please refer to these questions and answers to learn more about yourself:\
             {initial_context["responses"]}'}]
    print(f"You are speaking to {name}. type \"exit\" when you are finished")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("ending conversation")
            break
        else:
            context.append({"role": "user", "content": user_input})
            message = call_chat_w_context(context)
            context.append({"role": f"assistant", "content": message})
            play_voice(voice_id, message)


def main():
    print("Hello, would you like to build a new clone or interact with an existing one?")
    time.sleep(2)
    action = input("(build new) | (use existing): ").strip().lower()
    if action == "build new":
         build_clone()
    elif action == "use existing":
        name = input("Who would you like to talk to?: ")
        converse(name)
    else:
         print("Sorry, that was not one of the options. Please try again")
         main()    

if __name__ == "__main__":
    main()
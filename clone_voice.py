from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs
import os
import re

API_KEY = 'sk_f1da0f131c780c4dd0e1ec84a1ed579f412225e4f4fdef03'

client = ElevenLabs(api_key=API_KEY)

def add_voice(voice_name,voice_description,audio_directory,label = ''):
    samples = []
    for wav_file in os.listdir(audio_directory):
        samples.append(("files", open(f"{audio_directory}/{wav_file}", "rb")))

    voice = client.voices.add(
        name=voice_name,
        description=voice_description, # Optional
        files=samples,
        labels=label
    )

def play_voice(voice_id, text):

    audio = client.text_to_speech.convert(text=text, voice_id=voice_id)
    audio_bytes = b''.join(audio)
    #print(type(audio_bytes))

    play(audio_bytes)

'''
For testing
'''
#add_voice("Beth_test", "","Beth_4_audio_files")

# wav_file_paths = ["audio_files/Beth_Charolettes_Web.wav", "audio_files/Beth_Little_Prince.wav"]  # Replace with your actual wav file paths
# voice_name = "Beth_3"
# voice_description = "white american women in her late 20's"

# samples = []
# for wav_file_path in wav_file_paths:
#     samples.append(("files", open(wav_file_path, "rb")))


run = False
if run:
    add_voice("test_beth", "", "Beth_4_audio_files")

#returns voice id given a name
def voice_id_search(target):
    voice_list = client.voices.get_all()
    for voice_profile in voice_list.voices:
        if voice_profile.name == target:
            return voice_profile.voice_id
    return "could not find voice profile"

'''For testing
voice_id = voice_id_search("test_beth")

print(f"found voice id: {voice_id}")

# trained_voice = client.voices.get_all()
# voice_id = trained_voice.voices[-1].voice_id
# voice_name = trained_voice.voices[-1]
#client.voices.get()
# print(type(trained_voice.voices[-1]))


# voice_id='cd2FRRENiwcMNUxhbWh9'

# test_text = "Hi! I'm a cloned voice of Beth, a girl looking to get into UI UX."

'''

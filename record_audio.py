import pyaudio
import wave
import threading

def get_recording(person, question,directory):

    # Parameters
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1  # Mono
    fs = 44100  # Record at 44100 samples per second
    filename = f"{directory}/{person}_{question}.wav"

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames
    recording = True  # Flag to control recording

    def record_audio():
        print('Recording... Press enter/return to stop.')
        while recording:
            data = stream.read(chunk)
            frames.append(data)

    # Start recording in a separate thread
    thread = threading.Thread(target=record_audio)
    thread.start()

    # Wait for user input to stop the recording
    input()
    recording = False  # This will stop the recording loop
    thread.join()  # Wait for the recording thread to finish

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    print('Recording stopped. Audio saved to:', filename)
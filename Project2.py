#Author = Deep Gupta
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration = int(input("Enter the Duration of Recording"))

recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)

print("Record Your Recording.....")

sd.wait()
write("Rec.wav", freq, recording)

print("Completed... Your recording is saved as Rec")
print("Thank You")
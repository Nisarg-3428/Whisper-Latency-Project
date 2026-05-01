import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import time

# Load model once
print("🔄 Loading model...")
t0 = time.time()
model = whisper.load_model("small")
print(f"✅ Model loaded in {time.time() - t0:.2f}s\n")

def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎤 Recording...")
    start = time.time()

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)

    end = time.time()
    print(f"✅ Recording complete ({end - start:.2f}s)")
    return filename, end - start

def transcribe(audio_file):
    print("🧠 Transcribing...")
    start = time.time()

    result = model.transcribe(audio_file, language="en", fp16=False)

    end = time.time()
    print(f"✅ Transcription done ({end - start:.2f}s)")
    return result["text"], end - start

if __name__ == "__main__":
    total_start = time.time()

    audio_path, rec_time = record_audio(duration=5)
    text, trans_time = transcribe(audio_path)

    total_end = time.time()

    print("\n🧠 Transcription:")
    print(text)

    print("\n⏱️ Latency Breakdown:")
    print(f"Recording time     : {rec_time:.2f}s")
    print(f"Transcription time : {trans_time:.2f}s")
    print(f"Total time         : {total_end - total_start:.2f}s")
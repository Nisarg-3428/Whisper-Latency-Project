# Whisper Latency Project

## Overview
This project explores and benchmarks the latency of OpenAI Whisper-based speech-to-text processing. It focuses on measuring inference time and optimizing performance for real-time or near real-time applications.

---

## Features
- Speech-to-text transcription using Whisper
- Latency measurement and benchmarking
- Simple Python-based pipeline
- Modular structure for experimentation

---

## Project Structure
. ├── src/ │   └── whisper_runner.py   # Main script for running transcription ├── requirements.txt        # Dependencies └── .gitignore

---

## Installation

### 1. Clone the repository
bash git clone https://github.com/Nisarg-3428/Whisper-Latency-Project.git cd Whisper-Latency-Project 

### 2. Create virtual environment
bash python -m venv venv source venv/bin/activate   # Mac/Linux 

### 3. Install dependencies
bash pip install -r requirements.txt 

---

## Usage

Run the main script:

bash python src/whisper_runner.py 

You can modify the script to:
- Change input audio
- Adjust model size
- Measure latency for different configurations

---

## Example Output
- Transcribed text
- Time taken for processing
- Latency metrics

---

## Goals
- Reduce inference latency
- Evaluate performance across models
- Enable real-time speech applications

---

## Future Improvements
- Streaming transcription
- GPU optimization
- Batch processing support
- Visualization of latency metrics

---

## Requirements
- Python 3.8+
- FFmpeg (for audio processing)
- Compatible hardware (CPU/GPU)

---

## Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

---

## License
This project is open-source and available under the MIT License.

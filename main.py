import numpy as np
import soundfile as sf

class CircularDelay:
    def __init__(self, sample_rate, delay_time_ms, feedback, wet_mix):
        self.sample_rate = sample_rate
        self.delay_samples = int(sample_rate * delay_time_ms / 1000)
        self.buffer_length = self.delay_samples + 1
        self.delay_buffer = np.zeros((2, self.buffer_length))
        self.feedback = feedback
        self.wet_mix = wet_mix
        self.current_position = 0

    def process(self, input_sample):
        delay_sample = self.delay_buffer[:, self.current_position]
        output_sample = input_sample + self.wet_mix * delay_sample

        feedback_sample = delay_sample * self.feedback
        write_position = (self.current_position + self.delay_samples) % self.buffer_length
        self.delay_buffer[:, write_position] = input_sample + feedback_sample

        self.current_position = (self.current_position + 1) % self.buffer_length

        return output_sample

    def set_feedback(self, feedback):
        self.feedback = feedback

    def set_wet_mix(self, wet_mix):
        self.wet_mix = wet_mix

# Parameters
input_file = 'input_audio_stereo.wav'
output_file = 'output_audio_stereo.wav'
delay_time_ms = 250
initial_feedback = 0.6
initial_wet_mix = 0.5

# Read input audio
input_audio, sample_rate = sf.read(input_file, always_2d=True)

# Initialize the circular delay processor
processor = CircularDelay(sample_rate, delay_time_ms, initial_feedback, initial_wet_mix)

# Process the audio
output_audio = np.zeros_like(input_audio)
for i in range(len(input_audio)):
    output_audio[i] = processor.process(input_audio[i])

    # Adjust feedback and wet mix in real-time
    if i % 10000 == 0:
        new_feedback = float(input("Enter new feedback value (0-1): "))
        processor.set_feedback(new_feedback)
        new_wet_mix = float(input("Enter new wet mix value (0-1): "))
        processor.set_wet_mix(new_wet_mix)

# Write output audio
sf.write(output_file, output_audio, sample_rate)

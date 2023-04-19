# LexiconPCM70
CircularDelay Experiment for Lexicon PCM70

# How-to-Use
This code defines a CircularDelay class that processes stereo audio and allows you to adjust the feedback and wet mix at any time. The class maintains separate delay buffers for each audio channel (left and right). The process method applies the circular delay effect to the current input sample and updates the delay buffer. The set_feedback and set_wet_mix methods allow you to adjust the feedback and wet mix parameters in real-time.

In the `main.py`, the audio is processed sample by sample in a loop. Every 10,000 samples (approximately every 0.23 seconds at a 44.1 kHz sample rate), the user is prompted to enter new feedback and wet mix values. You can adjust this interval as needed or implement a different way to adjust these parameters in real-time.

Please note that this example uses the blocking input function for demonstration purposes. In a real-time audio processing application, you might want to use a different method to get user input or adjust parameters, such as a graphical user interface or MIDI controller.

# Pedal Implementation
Work-In-Progress but I had an idea to put inside FV-1. Constratint would be the memory and how extensive the DSP resource would handle extended delay time.
Check `CD.spn`

# Resources
`https://electric-canary.com/fv1start.html`

import winsound
import time

# Define the tempo (in beats per minute)
tempo = int(input("Enter the tempo (in beats per minute): "))

# Calculate the duration of a quarter note (in milliseconds)
quarter_note_duration = 60000 / tempo

# Define the frequencies and durations of the notes
note_freqs = []
note_durations = []

print("Enter the notes, one at a time. When you are done, enter an empty line.")

while True:
  note = input("Enter a note (e.g. C4, D4, E4, etc.): ")
  if note == "":
    break
  duration = input("Enter the duration (e.g. 1 for a whole note, 0.5 for a half note, etc.): ")
  note_freqs.append(int(note))
  note_durations.append(quarter_note_duration * float(duration))

# Iterate through the notes and play them
for freq, duration in zip(note_freqs, note_durations):
  winsound.Beep(freq, int(duration))
  time.sleep(duration / 1000)

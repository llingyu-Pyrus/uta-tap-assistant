from pydub import AudioSegment, silence
import json
import base64

# Remove the silence sections from vocal synthesizer
for i in range(1, 33):
    sound = AudioSegment.from_file('./data/untitled - Track {index}.wav'.format(index = str(i)), format = 'wav')
    leds = silence.detect_leading_silence(sound, -20)
    print(leds)
    sound[leds - 80 : leds + 320].export('./result/{index}.mp3'.format(index = str(i - 1)), format = 'mp3')

# Convert to base64 in format of xx.json
res = {}
for i in range(32):
    with open('./result/{index}.mp3'.format(index = i), 'rb') as s:
        res['{index}.mp3'.format(index = i)] = f'data:audio/mpeg;base64,' + base64.b64encode(s.read()).decode('utf-8')
with open('./result/kafu.json', 'w') as jn:
    json.dump(res, jn, indent = 4)
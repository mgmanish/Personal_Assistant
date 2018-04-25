import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
import os

def textspoken():
    os.system("record.py 1")
 
    speech_to_text = SpeechToTextV1(
    username='1cd4591b-5616-437f-b58b-ad2f4db49a0f',
    password='4n4hLVTKEqbW',
    x_watson_learning_opt_out=False
    )

    json.dumps(speech_to_text.models(), indent=2)

    json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2)

    with open(join(dirname(__file__),'output.wav'),
          'rb') as audio_file:
        x = json.dumps(speech_to_text.recognize(
        audio_file, content_type='audio/wav', timestamps=False,
        word_confidence=False),
    indent=2)
        y = json.loads(x)
    return (y['results'][0]['alternatives'][0]['transcript'])

if __name__ == '__main__':
    p = textspoken()
    print(p)

import requests
import json
from config import apiKey

qa = []
deep_context = 4
def apiCall(question):
    url = 'https://api.openai.com/v1/chat/completions'
    qa.append({"role": "user", "content": question})
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": qa,
        "temperature": 0.7
    }
    
    headers = {'content-type': 'application/json',"Authorization": "Bearer " + apiKey}

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r)
    ans = eval(r.text)
    zoraText = ans['choices'][0]['message']['content']
    qa.append(ans['choices'][0]['message'])

    if len(qa) >= deep_context:
        qa.clear()
        qa.append(ans['choices'][0]['message'])
    # print(qa)
    return zoraText


def speechToText(audioFile):
    # file audio gia aperto
    url = 'https://api.openai.com/v1/audio/transcriptions'

    payload = {
        "model": "whisper-1",
        "language": "it"
    }
    
    payload_file = {
        "file": audioFile
        
    }
    headers = {"Authorization": "Bearer " + apiKey}


    r = requests.post(url, data=payload, headers=headers, files=payload_file)
    
    ans = eval(r.content)
    return str(ans['text'])

if __name__ == '__main__':

    text = speechToText(open("temp.m4a", "rb"))
    # ans = apiCall('quanto fa 2+2')
    print(text)
    # print(ans.split('.'))

    print('\nFine')

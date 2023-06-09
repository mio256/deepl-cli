import os
import re
import requests
from dotenv import load_dotenv
load_dotenv()


def translate(text: str) -> str:
    if re.search(r'[ぁ-ん]+|[ァ-ヴー]+|[一-龠]+', text):
        source_lang = 'JA'
        target_lang = 'EN'
    else:
        source_lang = 'EN'
        target_lang = 'JA'

    params = {
        'auth_key': os.environ['DEEPL_TOKEN'],
        'text': text,
        'source_lang': source_lang,
        "target_lang": target_lang
    }

    return requests.post("https://api-free.deepl.com/v2/translate", data=params).json()['translations'][0]['text']

import json
import requests


class ToneAnalyzer:
    def __init__(self, text):
        self.username = '0283e965-ef1d-4737-ba70-c1eefcca4939'
        self.password = 'uJqpULCLFnjm'
        self.watson_url = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-18'
        self.headers = {"content-type": "text/plain"}
        self.data = text

    def analyze_tone(self):
        json_analyze = self.__analyze_tone()

        return self.__transform_results(json_analyze)

    def __analyze_tone(self):
        try:
            result = requests.post(self.watson_url, auth=(self.username, self.password),
                                   headers=self.headers, data=self.data.encode('utf8'))
            return result.text
        except():
            return False

    def __transform_results(self, json_analyze):
        analyze = json.loads(str(json_analyze))
        text_answer = ''
        for i in analyze['document_tone']['tone_categories']:
            text_answer += i['category_name'] + '\n' + ("-" * len(i['category_name'])) + '\n'
            for j in i['tones']:
                text_answer += j['tone_name'].ljust(20) + (str(round(j['score'] * 100, 1)) + "%").ljust(10) + '\n'
            text_answer += '\n'
        return text_answer


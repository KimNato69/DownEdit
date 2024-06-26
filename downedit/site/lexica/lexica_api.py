from colorama import *
import requests
import requests_random_user_agent

class LexicaAPI:
    def __init__(self) -> None:
        self.base_url = "https://lexica.art"
        self.search_endpoint = "/api/infinite-prompts"
        self.platform = "lexica-aperture-v3.5"
        
        self.headers = {
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ko-US;q=0.8,ko;q=0.7,hu-US;q=0.6,hu;q=0.5,km-GB;q=0.4,km;q=0.3',
            'Content-Length': '92',
            'Content-Type': 'application/json',
            'Origin': self.base_url,
            "Referer": self.base_url,
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site'
        }

    def _generate_user_agent(self):
        with requests.Session() as s:
            return s.headers['User-Agent']

    def search_img(self, prompt, amount):
        
        user_gen = self._generate_user_agent()
        self.headers['User-Agent'] = user_gen
        param = {"text": prompt, "model": self.platform, "searchMode": "images", "source": "search", "cursor": amount}

        with requests.Session() as s:
            response = s.post(
                self.base_url + self.search_endpoint,
                headers=self.headers,
                json=param
            )

            if response.status_code == 200:
                return response.json()
            else:
                return None


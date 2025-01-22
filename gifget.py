import requests

class GetGif:

    def __init__(self):
        self.params = {
            "api_key": "lcFTds1jFP1g7edgtdVjWsmqnvvFr7iI",
        }
        self.gif_url = "https://api.giphy.com/v1/gifs/random"


    def get_gif(self, condition):
        if condition:
            self.params["tag"] = "cheeseburger"
        else:
            self.params["tag"] = "crying"
        response = requests.get(url=self.gif_url, params=self.params)
        output = response.json()
        link = output["data"]["images"]["original"]["mp4"]
        return link


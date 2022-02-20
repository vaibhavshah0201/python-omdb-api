import requests
class Omdb:
    API_KEY = '7dcb20ae'
    param_keys = {}

    def __init__(self):
        self.param_keys = {
            'title' : 't',
            'id' : 'i',
        }        

    def get_param_keys(self):
        return self.param_keys.keys()
        
    def get_api_url(self):
        return 'http://www.omdbapi.com/?apikey='+self.API_KEY
    
    def get(self, key, param):
        url = self.get_api_url()
        return requests.get(url+"&"+self.param_keys[key]+"="+param)
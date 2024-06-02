class Config:
    def __init__(self):
        self.api_key = None

    def configure(self, api_key):
        self.api_key = api_key


config = Config()

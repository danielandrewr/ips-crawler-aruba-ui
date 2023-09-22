

class Test():
    def __init__(self):
        self.db_name = 'wifi_crawl'
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient('localhost', 27017)
            self.db = self.client[self.db_name]
            print("Connected to the MongoDB database successfully!")
        except Exception as e:
            print("An error occurred while connecting to the database:", e)

    def connect(self, uri):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[self.db_name]
            print("Connected to the MongoDB database successfully!")
        except Exception as e:
            print("An error occurred while connecting to the database:", e)
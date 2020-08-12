import pandas as pd


class DataHandler(object):
    def __init__(self, businesses_filename, review_filename):
        hotels_data = pd.read_json(businesses_filename, lines=True)
        self.hotels = hotels_data['id'].unique().tolist()
        self.hotels = list(map(str, self.hotels))

        self.reviews = pd.read_json(review_filename, lines=True)
        reviews_authors = pd.read_json(self.reviews["author"].to_json(orient='records'))
        self.users = reviews_authors["id"].unique().tolist()
        self.users.remove('')

import pandas as pd
from recordclass import recordclass
import json
import statistics

UserProfile = recordclass('UserProfile', 'id lives_in avg_service avg_cleanliness avg_overall '
                                         'avg_value avg_location avg_rooms')


class DataHandler(object):
    def __init__(self, businesses_filename, review_filename):
        # hotels_data = pd.read_json(businesses_filename, lines=True)
        # self.hotels = hotels_data['id'].unique().tolist()
        # self.hotels = list(map(str, self.hotels))

        self.reviews = pd.read_json(review_filename, lines=True)
        self.reviews_authors = pd.read_json(self.reviews['author'].to_json(orient='records'))
        self.users = self.reviews_authors["id"].unique().tolist()
        self.users.remove('')

        self.__user_profiles__ = []
        for user_id in self.users:
            user_reviews = self.__get_user_reviews__(user_id)
            user_profile = UserProfile(user_id, '', '', '', '', '', '', '')
            author = pd.read_json(user_reviews['author'].to_json(orient='records'))
            if 'location' in author.index:
                user_profile.lives_in = author['location']
            ratings = pd.read_json(user_reviews['ratings'].to_json(orient='records'))
            if 'service' in ratings.index:
                user_profile.avg_service = statistics.mean(ratings['service'].to_list())
            if 'cleanliness' in ratings.index:
                user_profile.avg_cleanliness = statistics.mean(ratings['cleanliness'].to_list())
            if 'overall' in ratings.index:
                user_profile.avg_overall = statistics.mean(ratings['overall'].to_list())
            if 'value' in ratings.index:
                user_profile.avg_value = statistics.mean(ratings['value'].to_list())
            if 'location' in ratings.index:
                user_profile.avg_location = statistics.mean(ratings['location'].to_list())
            if 'rooms' in ratings.index:
                user_profile.avg_rooms = statistics.mean(ratings['rooms'].to_list())
            self.__user_profiles__.append(user_profile)
            print(user_id)

        # all_groups = {}
        # locations = list(set([location if len(location.split(",")) <= 1 else location.split(",")[1]
        #                       for location in self.reviews_authors['location'].unique().tolist()]))
        # locations.remove('')
        # print(len(locations))

        exit()

    def __get_user_reviews__(self, user_id):
        indexes = []
        for index, row in self.reviews_authors.iterrows():
            if row['id'] == user_id:
                indexes.append(index)

        return self.reviews.loc[indexes]
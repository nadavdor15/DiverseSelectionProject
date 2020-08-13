import pandas as pd
from recordclass import recordclass
import statistics

UserProfile = recordclass('UserProfile', 'id lives_in avg_service avg_cleanliness avg_overall '
                                         'avg_value avg_location avg_rooms')


class DataHandler(object):
    def __init__(self, businesses_filename, review_filename):
        # hotels_data = pd.read_json(businesses_filename, lines=True)
        # self.hotels = hotels_data['id'].unique().tolist()
        # self.hotels = list(map(str, self.hotels))

        self.__reviews = pd.read_json(review_filename, lines=True)
        self.reviews_authors = pd.read_json(self.__reviews['author'].to_json(orient='records'))
        self.__users = self.reviews_authors["id"].unique().tolist()
        self.__users.remove('')

        range_names = [i + "_" + j for j in 'avg_service avg_cleanliness avg_overall' 
                                            ' avg_value avg_location avg_rooms'.split(' ')
                       for i in ["low", "medium", "high"]]
        self.__user_groups = {x: [] for x in range_names}

        self.__user_profiles__ = []
        for user_id in self.__users:
            user_reviews = self.__get_user_reviews(user_id)
            author = pd.read_json(user_reviews['author'].to_json(orient='records'))
            ratings = pd.read_json(user_reviews['ratings'].to_json(orient='records'))
            self.__add_user_to_groups(user_id, author, ratings)

    def __add_user_to_groups(self, user_id, author, ratings):
        user_profile = UserProfile('', '', '', '', '', '', '', '')
        if 'location' in author.columns:
            user_profile.lives_in = author['location'].to_list()[0]
            if len(user_profile.lives_in.split(",")) > 1:
                user_profile.lives_in = user_profile.lives_in.split(",")[1]
            if user_profile.lives_in not in self.__user_groups:
                self.__user_groups[user_profile.lives_in] = []
            self.__user_groups[user_profile.lives_in].append(user_id)
        ratings_names = [name[4:] for name in UserProfile.__dict__.keys() if name.startswith('avg_')]
        for name in ratings_names:
            self.__add_user_to_property_group(user_id, user_profile, ratings, name)

    def __add_user_to_property_group(self, user_id, user_profile, ratings, property):
        if property in ratings.columns:
            user_profile.avg_service = statistics.mean(ratings[property].to_list())
            if user_profile.avg_service < 2:
                self.__user_groups['low_avg_' + property].append(user_id)
            elif user_profile.avg_service < 3.5:
                self.__user_groups['medium_avg_' + property].append(user_id)
            else:
                self.__user_groups['high_avg_' + property].append(user_id)

    def __get_user_reviews(self, user_id):
        indexes = []
        for index, row in self.reviews_authors.iterrows():
            if row['id'] == user_id:
                indexes.append(index)

        return self.__reviews.loc[indexes]

    @property
    def groups(self):
        return list(self.__user_groups.values())

    @property
    def users(self):
        return self.__users

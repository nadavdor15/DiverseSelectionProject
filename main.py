from BaseDiversitySolver import *
from DataHandler import *

businesses_filename = 'C:\\Users\\revcr\\Downloads\\review\\offering.json'
reviews_filename = 'C:\\Users\\revcr\\Downloads\\review\\review_1.json'


def main():
    # running example
    # users = ['Alice', 'Bob', 'Carol', 'David', 'Eve']
    # groups = [['Alice', 'David'], ['Bob'], ['Carol'], ['Eve'],
    #           ['Alice', 'Carol'],
    #           ['Bob'], ['Alice', 'David', 'Eve'],
    #           ['Bob'], ['Eve', 'David'], ['Alice'],
    #           ['Alice'], ['Carol', 'Eve'], ['Bob'],
    #           ['Carol', 'Eve'], ['Alice'], ['Bob']]

    data_handler = DataHandler(businesses_filename, reviews_filename)
    users = data_handler.users
    groups = users
    solver = BaseDiversitySolver(users, groups)
    print(solver.solve(bucket_size=2, weight='LBS', cover='Single'))


if __name__ == "__main__":
    main()

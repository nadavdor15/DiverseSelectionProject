from BaseDiversitySolver import *
from DataHandler import *
from os import path
from pickle import dump, load

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
    # groups = [list(tup) for tup in set(tuple(x) for x in groups)]
    data_handler = None
    file_name = 'data_handler_1.pkl'
    if path.exists(file_name):
        with open(file_name, 'rb') as f:
            data_handler = load(f)
            print("done reading data")
    else:
        data_handler = DataHandler(businesses_filename, reviews_filename)
        print("done building data")
        with open(file_name, 'wb') as f:
            dump(data_handler, f)

    users = data_handler.users
    groups = data_handler.groups
    solver = BaseDiversitySolver(users, groups)
    solution = solver.solve(bucket_size=4, weight='LBS', cover='Single')
    print("Selected users:", solution.users)
    print("Amount of represented groups:", len(solution.groups))
    print("Total amount of groups:", len(groups))


if __name__ == "__main__":
    main()

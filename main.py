# from BaseDiversitySolver import *
# from DataHandler import *
# from os import path
# from pickle import dump, load
from MRBaseDiversitySolver import *


def main():
    # This is a running example of the regular algorithm.

    # users = ['Alice', 'Bob', 'Carol', 'David', 'Eve']
    # groups = [['Alice', 'David'], ['Bob'], ['Carol'], ['Eve'],
    #           ['Alice', 'Carol'],
    #           ['Bob'], ['Alice', 'David', 'Eve'],
    #           ['Bob'], ['Eve', 'David'], ['Alice'],
    #           ['Alice'], ['Carol', 'Eve'], ['Bob'],
    #           ['Carol', 'Eve'], ['Alice'], ['Bob']]
    # groups = [list(tup) for tup in set(tuple(x) for x in groups)]

    # businesses_filename = 'C:\\Users\\revcr\\Downloads\\review\\offering.json'
    # reviews_filename = 'C:\\Users\\revcr\\Downloads\\review\\review_1.json'
    # data_handler = None
    # file_name = 'data\\pickles\\data_handler_1.pkl'
    # if path.exists(file_name):
    #     with open(file_name, 'rb') as f:
    #         data_handler = load(f)
    #         print("done reading data")
    # else:
    #     data_handler = DataHandler(businesses_filename, reviews_filename)
    #     print("done building data")
    #     with open(file_name, 'wb') as f:
    #         dump(data_handler, f)
    #
    # users = data_handler.users
    # groups = data_handler.groups

    # with open('users_dh_1.csv', 'w') as f:
    #     for user in users:
    #         f.write("%s\n" % user)
    #
    # with open('groups_dh_1.csv', 'w') as f:
    #     for i in range(len(groups)):
    #         f.write("%d, %s\n" % (i+1, groups[i]))
    # solver = BaseDiversitySolver(users, groups)
    # solution = solver.solve(bucket_size=4, weight='LBS', cover='Single')
    # print("\n#########################")
    # print("Results:")
    # print("Selected users:", solution.users)
    # print("Amount of represented groups:", len(solution.groups))
    # print("Total amount of groups:", len(groups))

    # This is a running example of the MapReduce algorithm.

    MRBaseDiversitySolver.run()


if __name__ == "__main__":
    main()

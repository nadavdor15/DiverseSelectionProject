from BaseDiversitySolver import *


def main():
    users = ['Alice', 'Bob', 'Carol', 'David', 'Eve']
    groups = [['Alice', 'David'], ['Bob'], ['Carol'], ['Eve'],
              ['Alice', 'Carol'],
              ['Bob'], ['Alice', 'David', 'Eve'],
              ['Bob'], ['Eve', 'David'], ['Alice'],
              ['Alice'], ['Carol', 'Eve'], ['Bob'],
              ['Carol', 'Eve'], ['Alice'], ['Bob']]
    solver = BaseDiversitySolver(users, groups)
    print(solver.solve(bucket_size=2, weight='LBS', cover='Single'))


if __name__ == "__main__":
    main()

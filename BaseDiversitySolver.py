from recordclass import recordclass
from math import floor

User = recordclass('User', 'id marg groups')
Group = recordclass('Group', 'id wei cov users')


class BaseDiversitySolver(object):
    def __init__(self, users, groups):
        self.users = [User(user, None, []) for user in users]
        self.groups = [Group(i, None, None, []) for i in range(len(groups))]
        for user in self.users:
            for group in self.groups:
                if user.id in groups[group.id]:
                    group.users.append(user)
                    user.groups.append(group)

    def solve(self, bucket_size, weight='LBS', cover='Single'):
        solution = []
        for group in self.groups:
            group.wei, group.cov = self.weight(group, weight, len(solution)),\
                                   self.cover(group, cover, len(solution))
        for user in self.users:
            user.marg = BaseDiversitySolver.marg(user)

        for i in range(bucket_size):
            if len(self.users) == 0:
                break
            users_margs = [user.marg for user in self.users]
            max_user_idx = users_margs.index(max(users_margs))
            max_user = self.users[max_user_idx]
            solution.append(max_user.id)
            self.users.remove(max_user)
            for group in self.groups:
                if group.cov > 0 and max_user in group.users:
                    group.cov -= 1
                    if group.cov == 0:
                        for user in group.users:
                            user.marg -= group.wei

        return solution

    def weight(self, group, type, subset_size):
        if type == 'Iden':
            return 1
        elif type == 'LBS':
            return len(group.users)
        elif type == 'EBS':
            order = sorted(self.groups, key=lambda group: len(group.users)).index(group) + 1
            return (subset_size + 1)**order
        else:
            raise Exception('Unsupported weight function')

    def cover(self, group, type, subset_size):
        if type == 'Single':
            return 1
        elif type == 'Prop':
            return max(floor((len(group.users)*subset_size)/len(self.users)),1)
        else:
            raise Exception('Unsupported cover function')

    @staticmethod
    def marg(user):
        return sum([group.wei for group in user.groups])

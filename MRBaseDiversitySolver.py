from mrjob.job import MRJob, MRStep
import ast


class MRBaseDiversitySolver(MRJob):
    def steps(self):
        return [MRStep(mapper=self.retrieve_user_groups,
                       reducer=self.reducer_to_list),
                MRStep(mapper=self.retrieve_marg,
                       reducer=self.reducer_to_list),
                MRStep(mapper=self.retrieve_max_user_mapper,
                       reducer=self.retrieve_max_user_reducer),]

    def retrieve_user_groups(self, _, line):
        index, group = line.split(', ', 1)
        group = ast.literal_eval(group)
        for user in group:
            yield (user, group)

    def reducer_to_list(self, user, groups):
        yield (user, list(groups))

    def retrieve_marg(self, user, groups):
        marg = sum([len(group) for group in groups])
        # should be a random number from [1, numOfMappers] instead of 1
        yield (1, [user, marg, groups])

    def retrieve_max_user_mapper(self, _, values):
        part_max_marg, part_max_user = -1, None
        for value in values:
            user, marg, marg_and_group = value[0], value[1], value[1:]
            yield (user, marg_and_group)
            if marg > part_max_marg:
                part_max_marg = marg
                part_max_user = user
        yield ('$part_max_user', part_max_user)

    def retrieve_max_user_reducer(self, key, values):
        if key == '$part_max_user':
            # write to hdfs file instead of yield
            yield ('$max_user', max(values))
        else:
            yield (key, list(values))

    def remove_max_user(self, user, value):
        if self.max != user:
            marg = value[0]
            groups = value[1]
            for group in groups:
                if self.max in group:
                    marg -= len(group)
                yield (user, [marg, groups])

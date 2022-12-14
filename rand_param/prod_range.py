class Prod_range(object):
    def __init__(self, int_list):
        self.n_ranges = len(int_list)
        self.ranges = int_list
        self.total_length = 1
        for r in int_list:
            self.total_length *= r

    def iget(self, idx):
        if (idx < 0):
            idx = self.total_length + idx
        if (idx >= self.total_length):
            raise IndexError(
                "{} object index out of range".format(self.__class__.__name__))
        output = [0] * self.n_ranges
        which_range = self.n_ranges - 1
        while ((idx > 0) and (which_range >= 0)):
            current_range = self.ranges[which_range]
            output[which_range] = idx % current_range
            which_range -= 1
            idx = idx // current_range
        return tuple(output)

    def __len__(self):
        "Return len(self)."
        return self.total_length

    def __getitem__(self, key):
        return self.iget(key)

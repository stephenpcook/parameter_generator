from . import Prod_range

class Product(object):
    def __init__(self, iterables):
        lengths = [len(it) for it in iterables]
        self.iterables = iterables
        self.product_indices = Prod_range(lengths)

    def __len__(self):
        return len(self.product_indices)

    def __getitem__(self, key):
        if key > len(self):
            raise IndexError(
                "{} object index out of range".format(self.__class__.__name__))
        indices = self.product_indices[key]
        return tuple(it[idx] for it, idx in zip(self.iterables, indices))


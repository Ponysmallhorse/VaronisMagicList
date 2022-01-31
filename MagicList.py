
class MagicList(list):
    def __init__(self, cls_type=None):
        self.csl_type = cls_type
        super().__init__()

    def __setitem__(self, key: int, value):
        if self.csl_type is not None and not isinstance(value, self.csl_type):
            raise ValueError("Incorrect Value type")
        elif key < 0:
            raise IndexError("Invalid Index")
        elif key - 1 > len(self):
            raise IndexError("Index out of Range")
        elif key < len(self):
            super().__setitem__(key, value)
        elif key == len(self):
            self.append(value)

    def __getitem__(self, item):
        if item < len(self):
            return super().__getitem__(item)
        elif item == len(self):
            self.append(self.csl_type())
            return self[-1]
        else:
            raise IndexError("Index out of Range")


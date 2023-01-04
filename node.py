class Node:
    def __init__(self, key, occurrence=None):
        self.key = key
        self.occurrence = occurrence

        self.left = None
        self.right = None

    # less than
    def __lt__(self, other):
        return self.occurrence < other.occurrence

    # equal to
    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.occurrence == other.occurrence

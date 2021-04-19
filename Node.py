class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{str(self.value)}->{str(self.next)}"


if __name__ == '__main__':
    pass

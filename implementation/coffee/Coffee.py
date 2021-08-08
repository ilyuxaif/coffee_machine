class Coffee:
    type: str
    size: str
    sugar: int

    def __init__(self, type, size, sugar):
        self.type = type
        self.size = size
        self.sugar = sugar

        print(f'You\'ve made {size} of {type} with {sugar} pieces of sugar.')
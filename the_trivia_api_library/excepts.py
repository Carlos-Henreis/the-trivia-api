class TriviaAPIException(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidTriviaCategoryError(Exception):
    """Raised when an invalid trivia category is specified."""

    def __init__(self, category):
        super().__init__(f"Invalid trivia category: {category}")
        self.category = category

class InvalidTriviaOrderError(Exception):
    """Raised when an invalid trivia order is specified."""

    def __init__(self, invalid_order):
        super().__init__(f"Invalid order: {invalid_order}")

class InvalidTriviaDifficultyError(Exception):
    """Raised when an invalid trivia difficulty is specified."""

    def __init__(self, invalid_difficulty):
        super().__init__(f"Invalid difficulty: {invalid_difficulty}")

class InvalidTriviaTypeError(Exception):
    """Raised when an invalid trivia type is specified."""

    def __init__(self, invalid_type):
        super().__init__(f"Invalid type: {invalid_type}")
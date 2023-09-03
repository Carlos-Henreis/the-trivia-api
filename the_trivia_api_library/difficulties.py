from .enums.enum_difficulty import EnumDifficulty
from .excepts import InvalidTriviaDifficultyError

class TriviaDifficulty:
    """Trivia difficulties."""

    _difficulties = None
    def __init__(self, difficulties=None):
        """
        TriviaDifficulty constructor.
        :param difficulties: list of difficulties
        :return: TriviaDifficulty object
        """

        self._difficulties = difficulties or []

        if difficulties is None:
            self._difficulties = []
        else:
            enum_values = {member.value for member in EnumDifficulty}
            invalid_difficulties = [element for element in difficulties if element not in enum_values]

            if invalid_difficulties:
                raise InvalidTriviaDifficultyError(invalid_difficulties)

        self._difficulties = difficulties or []

    def add_difficulty(self, difficulty):
        """
        Add a difficulty to the list of difficulties.
        :param difficulty: difficulty to be added
        :return: None
        """
        enum_values = {member.value for member in EnumDifficulty}
        if (difficulty in enum_values) and difficulty not in self._difficulties:
            self._difficulties.append(difficulty)
        else:
            raise InvalidTriviaDifficultyError(difficulty)

    def to_query_string(self):
        """
        Convert the list of difficulties to a query string.
        :param: None
        :return: query string
        """

        return ','.join(self._difficulties) or None
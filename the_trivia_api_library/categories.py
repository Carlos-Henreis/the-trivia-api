from .enums.enum_category import EnumCategory
from .excepts import InvalidTriviaCategoryError

class TriviaCategory:
    """Trivia categories."""

    _categories = None
    def __init__(self, categories=None):
        """
        TriviaCategory constructor.
        :param categories: list of categories
        :return: TriviaCategory object
        """

        if categories is None:
            self._categories = []
        else:
            enum_values = {member.value for member in EnumCategory}
            invalid_categories = [element for element in categories if element not in enum_values]

            if invalid_categories:
                raise InvalidTriviaCategoryError(invalid_categories)

        self._categories = categories or []

    def add_category(self, category):
        """
        Add a category to the list of categories.
        :param category: category to be added
        :return: None
        """
        enum_values = {member.value for member in EnumCategory}
        if (category in enum_values) and category not in self._categories:
            self._categories.append(category)
        else:
            raise InvalidTriviaCategoryError(category)

    def to_query_string(self):
        """
        Convert the list of categories to a query string.
        :param: None
        :return: query string
        """

        return ','.join(self._categories) or None



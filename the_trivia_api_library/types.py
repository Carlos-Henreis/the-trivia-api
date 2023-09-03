from .enums.enum_type_question import EnumTypeQuestion
from .excepts import InvalidTriviaTypeError

class TriviaTypes:
    """Trivia type."""

    _types = None

    def __init__(self, types=None):
        """
        TriviaType constructor.
        :param types: list of types
        :return: TriviaType object
        """

        self._types = types or []

        if types is None:
            self._types = []
        else:
            enum_values = {member.value for member in EnumTypeQuestion}
            invalid_types = [element for element in types if element not in enum_values]

            if invalid_types:
                raise InvalidTriviaTypeError(invalid_types)

        self._types = types or []

    def add_type(self, type):
        """
        Add a type to the list of types.
        :param type: type to be added
        :return: None
        """
        enum_values = {member.value for member in EnumTypeQuestion}
        if (type in enum_values) and type not in self._types:
            self._types.append(type)
        else:
            raise InvalidTriviaTypeError(type)

    def to_query_string(self):
        """
        Convert the list of types to a query string.
        :param: None
        :return: query string
        """

        return ','.join(self._types) or None
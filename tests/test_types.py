#Tests unity for `TriviaTypes` class.

import pytest
from the_trivia_api_library.enums.enum_type_question import EnumTypeQuestion
from the_trivia_api_library.types import TriviaTypes
from the_trivia_api_library.excepts import InvalidTriviaTypeError


class TestTriviaTypes:
    """Test TriviaTypes class."""

    def test_init(self):
        """Test TriviaTypes constructor."""

        # test with no types
        trivia_types = TriviaTypes()
        assert trivia_types._types == []

        # test with valid types
        types = [EnumTypeQuestion.IMAGE_CHOICE.value, EnumTypeQuestion.TEXT_CHOICE.value]
        trivia_types = TriviaTypes(types)
        assert trivia_types._types == types

        # test with invalid types
        types = ['invalid_type']
        with pytest.raises(InvalidTriviaTypeError):
            trivia_types = TriviaTypes(types)

    def test_add_type(self):
        """Test add_type method."""

        # test with valid type
        trivia_types = TriviaTypes()
        trivia_types.add_type(EnumTypeQuestion.TEXT_CHOICE.value)
        assert trivia_types._types == [EnumTypeQuestion.TEXT_CHOICE.value]

        # test with invalid type
        with pytest.raises(InvalidTriviaTypeError):
            trivia_types.add_type('invalid_type')

        # test with duplicate type
        with pytest.raises(InvalidTriviaTypeError):
            trivia_types.add_type(EnumTypeQuestion.TEXT_CHOICE.value)

    def test_to_query_string(self):
        """Test to_query_string method."""

        # test with no types
        trivia_types = TriviaTypes()
        assert trivia_types.to_query_string() is None

        # test with valid types
        types = [EnumTypeQuestion.IMAGE_CHOICE.value, EnumTypeQuestion.TEXT_CHOICE.value]
        trivia_types = TriviaTypes(types)
        assert trivia_types.to_query_string() == f'{EnumTypeQuestion.IMAGE_CHOICE.value},{EnumTypeQuestion.TEXT_CHOICE.value}'
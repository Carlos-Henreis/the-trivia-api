"""
test_categories
----------------------------------


"""

import pytest
from the_trivia_api_library.categories import TriviaCategory
from the_trivia_api_library.enums.enum_category import EnumCategory
from the_trivia_api_library.excepts import InvalidTriviaCategoryError


class TestTriviaCategory:
    """Test TriviaCategory class."""

    def test_init(self):
        """Test TriviaCategory constructor."""

        # test with no categories
        trivia_category = TriviaCategory()
        assert trivia_category._categories == []

        # test with valid categories
        categories = [EnumCategory.MUSIC.value, EnumCategory.GEOGRAPHY.value, EnumCategory.GENERAL_KNOWLEDGE.value]
        trivia_category = TriviaCategory(categories)
        assert trivia_category._categories == categories

        # test with invalid categories
        categories = ['invalid_category']
        with pytest.raises(InvalidTriviaCategoryError):
            trivia_category = TriviaCategory(categories)

    def test_add_category(self):
        """Test add_category method."""

        # test with valid category
        trivia_category = TriviaCategory()
        trivia_category.add_category(EnumCategory.MUSIC.value)
        assert trivia_category._categories == [EnumCategory.MUSIC.value]

        # test with invalid category
        with pytest.raises(InvalidTriviaCategoryError):
            trivia_category.add_category('invalid_category')

        # test with duplicate category
        with pytest.raises(InvalidTriviaCategoryError):
            trivia_category.add_category(EnumCategory.MUSIC.value)

    def test_to_query_string(self):
        """Test to_query_string method."""

        # test with no categories
        trivia_category = TriviaCategory()
        assert trivia_category.to_query_string() is None

        # test with valid categories
        categories = [EnumCategory.MUSIC.value, EnumCategory.GEOGRAPHY.value, EnumCategory.GENERAL_KNOWLEDGE.value]
        trivia_category = TriviaCategory(categories)
        assert trivia_category.to_query_string() == f'{EnumCategory.MUSIC.value},{EnumCategory.GEOGRAPHY.value},{EnumCategory.GENERAL_KNOWLEDGE.value}'

        # test with invalid categories
        categories = ['invalid_category']
        with pytest.raises(InvalidTriviaCategoryError):
            trivia_category = TriviaCategory(categories)
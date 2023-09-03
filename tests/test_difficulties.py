import pytest
from the_trivia_api_library.difficulties import TriviaDifficulty
from the_trivia_api_library.enums.enum_difficulty import EnumDifficulty
from the_trivia_api_library.excepts import InvalidTriviaDifficultyError


class TestTriviaDifficulty:
    """Test TriviaDifficulty class."""

    def test_init(self):
        """Test TriviaDifficulty constructor."""

        # test with no difficulties
        trivia_difficulty = TriviaDifficulty()
        assert trivia_difficulty._difficulties == []

        # test with valid difficulties
        difficulties = [EnumDifficulty.EASY.value, EnumDifficulty.MEDIUM.value, EnumDifficulty.HARD.value]
        trivia_difficulty = TriviaDifficulty(difficulties)
        assert trivia_difficulty._difficulties == difficulties

        # test with invalid difficulties
        difficulties = ['invalid_difficulty']
        with pytest.raises(InvalidTriviaDifficultyError):
            trivia_difficulty = TriviaDifficulty(difficulties)

    def test_add_difficulty(self):
        """Test add_difficulty method."""

        # test with valid difficulty
        trivia_difficulty = TriviaDifficulty()
        trivia_difficulty.add_difficulty(EnumDifficulty.EASY.value)
        assert trivia_difficulty._difficulties == [EnumDifficulty.EASY.value]

        # test with invalid difficulty
        with pytest.raises(InvalidTriviaDifficultyError):
            trivia_difficulty.add_difficulty('invalid_difficulty')

        # test with duplicate difficulty
        with pytest.raises(InvalidTriviaDifficultyError):
            trivia_difficulty.add_difficulty(EnumDifficulty.EASY.value)

    def test_to_query_string(self):
        """Test to_query_string method."""

        # test with no difficulties
        trivia_difficulty = TriviaDifficulty()
        assert trivia_difficulty.to_query_string() is None

        # test with valid difficulties
        difficulties = [EnumDifficulty.EASY.value, EnumDifficulty.MEDIUM.value, EnumDifficulty.HARD.value]
        trivia_difficulty = TriviaDifficulty(difficulties)
        assert trivia_difficulty.to_query_string() == f'{EnumDifficulty.EASY.value},{EnumDifficulty.MEDIUM.value},{EnumDifficulty.HARD.value}'
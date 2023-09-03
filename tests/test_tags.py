#create test unity for the_trivia_api_library\tags.py
# Path: tests\test_tags.py

import pytest
from the_trivia_api_library.tags import TriviaTags


class TestTriviaTag:
    """Test TriviaTag class."""

    def test_init(self):
        """Test TriviaTag constructor."""

        # test with no tags
        trivia_tag = TriviaTags()
        assert trivia_tag._tags == []

        # test with valid tags
        tags = ['test', 'vasco', 'football']
        trivia_tag = TriviaTags(tags)
        assert trivia_tag._tags == tags

    def test_add_tag(self):
        """Test add_tag method."""

        # test with valid tag
        trivia_tag = TriviaTags()
        trivia_tag.add_tag('test2')
        assert trivia_tag._tags == ['test2']


    def test_to_query_string(self):
        """Test to_query_string method."""

        # test with no tags
        trivia_tag = TriviaTags()
        assert trivia_tag.to_query_string() is None

        # test with valid tags
        tags = ['test', 'vasco', 'football']
        trivia_tag = TriviaTags(tags)
        assert trivia_tag.to_query_string() == f'{tags[0]},{tags[1]},{tags[2]}'
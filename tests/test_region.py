from the_trivia_api_library.region import TriviaRegion


class TestTriviaRegion:
    """Test TriviaRegion class."""

    def test_init(self):
        """Test TriviaRegion constructor."""

        # test with no regions
        trivia_region = TriviaRegion()
        assert trivia_region._region == ''

        # test with valid regions
        trivia_region = TriviaRegion('BR')
        assert trivia_region._region == 'BR'

    def test_add_region(self):
        """Test add_region method."""

        # test with valid region
        trivia_region = TriviaRegion()
        trivia_region.add_region('BR')
        assert trivia_region._region == 'BR'

    def test_to_query_string(self):
        """Test to_query_string method."""

        # test with no regions
        trivia_region = TriviaRegion()
        assert trivia_region.to_query_string() is None

        # test with valid regions
        trivia_region = TriviaRegion('BR')
        assert trivia_region.to_query_string() == 'BR'
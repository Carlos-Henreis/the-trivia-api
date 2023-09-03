#create test unity for the_trivia_api_library\client.py

import pytest
from the_trivia_api_library.client import TriviaAPIClient
from the_trivia_api_library.enums.enum_difficulty import EnumDifficulty
from the_trivia_api_library.enums.enum_order import EnumOrder


class TestTriviaAPIClient:

    def test_init(self):
        """Test TriviaAPIClient constructor."""

        # test with no parameters
        trivia_api_client = TriviaAPIClient()
        assert trivia_api_client._base_url == 'https://the-trivia-api.com/v2'


        # test with parameters
        trivia_api_client = TriviaAPIClient('api-token')
        assert trivia_api_client._base_url == 'https://the-trivia-api.com/v2'
        assert trivia_api_client._api_key == 'api-token'


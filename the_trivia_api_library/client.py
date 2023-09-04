import requests
from .categories import TriviaCategory
from .difficulties import TriviaDifficulty
from .tags import TriviaTags
from .region import TriviaRegion
from .types import TriviaTypes
from .excepts import TriviaAPIException

class TriviaAPIClient:
    def __init__(self, api_key=None):
        """
        TriviaAPIClient constructor.
        :param api_key: API key
        """
        self._base_url = 'https://the-trivia-api.com/v2'
        self._api_key = api_key


    def get_all_tags(self):
        """
        Get all tags.
        :param: None
        :return: list of tags
        """
        return self._make_api_request('GET', 'tags')

    def get_totals_per_tag(self, categories=None, difficulties=None, tags=None, region=None, types=None):
        """
        Get totals per tag.
        :param categories: list of categories
        :param difficulties: list of difficulties
        :param tags: list of tags
        :param region: list of regions
        :param types: list of types
        :return: list of totals per tag
        """
        params = {
            'categories': TriviaCategory(categories).to_query_string(),
            'difficulties': TriviaDifficulty(difficulties).to_query_string(),
            'region': TriviaRegion(region).to_query_string(),
            'tags': TriviaTags(tags).to_query_string(),
            'types': TriviaTypes(types).to_query_string(),
        }

        return self._make_api_request('GET', 'totals-per-tag', params)

    def get_random_question(self, limit=None, categories=None, difficulties=None, region=None, tags=None, types=None, session=None, preview=None):
        """
        Get a random set of questions.
        :param limit: number of questions
        :param categories: list of categories
        :param difficulties: list of difficulties
        :param region: list of regions
        :param tags: list of tags
        :param types: list of types
        :param session: session token
        :param preview: preview
        :return: list of questions
        """
        params = {
            'limit': limit or None,
            'categories': TriviaCategory(categories).to_query_string(),
            'difficulties': TriviaDifficulty(difficulties).to_query_string(),
            'region': TriviaRegion(region).to_query_string(),
            'tags': TriviaTags(tags).to_query_string(),
            'types': TriviaTags(types).to_query_string(),
            'order': TriviaTypes(types).to_query_string(),
            'session': session or None,
            'preview': preview or None,
        }

        return self._make_api_request('GET', 'questions', params)

    def _make_api_request(self, method, endpoint, params=None):
        """
        Make an API request.
        :param method: method
        :param endpoint: endpoint
        :param params: parameters
        :return: response
        """

        headers = {
            'X-API-Key': self._api_key,
            'Content-Type': 'application/json',
        }

        url = f'{self._base_url}/{endpoint}'

        response = requests.request(method, url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise TriviaAPIException("Unauthorized: Check your API X-API-Key")
        else:
            raise TriviaAPIException(f"Error while making the API request: {response.status_code}")
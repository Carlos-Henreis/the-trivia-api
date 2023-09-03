class TriviaRegion:
    """
    A class that represents the regions of the trivia API.
    """
    _region = None
    def __init__(self, region=None):
        self._region = region or ""

    def add_region(self, region):
        self._region = region

    def to_query_string(self):
        return self._region or None
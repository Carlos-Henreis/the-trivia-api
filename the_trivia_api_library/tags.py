class TriviaTags:
    """TriviaTags is a class that represents the tags parameter in the Trivia API."""

    _tags = []
    def __init__(self, tags=None):
        self._tags = tags or []

    def add_tag(self, tag):
        self._tags.append(tag)

    def to_query_string(self):
        return ','.join(self._tags) or None
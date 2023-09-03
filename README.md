# The Trivia API Python Library

![License](https://img.shields.io/badge/license-MIT-blue.svg)

A Python library for interacting with the Trivia API. This library allows you to easily request multiple-choice trivia questions and access various features of the Trivia API.

## Installation

You can install this library using pip:
```bash
pip install the-trivia-api-library
```

## Example usage
Here's an example of how to use this library to interact with the Trivia API:

```Python
from the_trivia_api import TriviaAPIClient, TriviaCategory, TriviaOrder, TriviaDifficulty, TriviaTags

# Initialize the Trivia API client
api_key = "YOUR_API_KEY"
client = TheTriviaAPIClient(api_key)

# Get a random set of questions
questions = client.get_random_questions(
    limit=5,
    categories=[TriviaCategory.GENERAL_KNOWLEDGE],
    difficulties=[TriviaDifficulty.EASY],
    tags=[TriviaTags.SCIENCE]
)

for question in questions:
    print(f"Question: {question['question']['text']}")
    print(f"Correct Answer: {question['correctAnswer']}")
    print(f"Incorrect Answers: {', '.join(question['incorrectAnswers'])}")
    print()
```

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute to the library, please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This library is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
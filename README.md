# The Trivia API Python Library
[![PyPI version](https://img.shields.io/pypi/v/the-trivia-api-library.svg)](https://pypi.org/project/the-trivia-api-library/)
[![PyPI downloads](https://img.shields.io/pypi/dm/the-trivia-api-library.svg)](https://pypi.org/project/the-trivia-api-library/)
![Python Versions](https://img.shields.io/pypi/pyversions/the-trivia-api-library)
![License](https://img.shields.io/pypi/l/the-trivia-api-library)

---

A Python library for interacting with the Trivia API. This library allows you to easily request multiple-choice trivia questions and access various features of the Trivia API.

## Demo

Access a demo of this library [here](https://demo-the-trivia-api-python.cahenre.com.br).

![example demo](https://raw.githubusercontent.com/Carlos-Henreis/the-trivia-api/master/docs/example-demo.png)


## Installation

You can install this library using pip:
```bash
pip install the_trivia_api_library
```

## Example usage
Here's an example of how to use this library to interact with the Trivia API:

```Python
from the_trivia_api_library import TriviaAPIClient, EnumCategory, EnumDifficulty

# Initialize the Trivia API client
api_key = "YOUR_API_KEY" # it's not necessary
client = TriviaAPIClient(api_key=api_key)

# Get a random set of questions
questions = client.get_random_question(
    limit=5,
    categories=[EnumCategory.SCIENCE.value],
    difficulties=[EnumDifficulty.EASY.value],
    tags=["math", "physics"]
)

for question in questions:
    print(f"Question: {question['question']['text']}")
    print(f"Correct Answer: {question['correctAnswer']}")
    print(f"Incorrect Answers: {', '.join(question['incorrectAnswers'])}")
    print()
```

## Methods

### get_random_question
Get a random set of questions from the Trivia API.

#### Parameters
- `limit` - The number of questions to return. Defaults to 1.
- `categories` - A list of categories to filter the questions by. Defaults to None.
- `difficulties` - A list of difficulties to filter the questions by. Defaults to None.
- `region` - A list of regions to filter the questions by. Defaults to None.
- `tags` - A list of tags to filter the questions by. Defaults to None.
- `types` - A list of types to filter the questions by. Defaults to None.
- `session` - A session object to use for the request. Defaults to None.
- `preview` - A boolean indicating whether to return the questions in preview mode. Defaults to False.

#### Returns
A list of questions.

#### Example
```Python
from the_trivia_api_library import TriviaAPIClient, EnumCategory, EnumDifficulty

# Initialize the Trivia API client
api_key = "YOUR_API_KEY"
client = TriviaAPIClient(api_key=api_key)

# Get a random set of questions
questions = client.get_random_question(
    limit=5,
    categories=[EnumCategory.SCIENCE.value],
    difficulties=[EnumDifficulty.EASY.value],
    tags=["math", "physics"]
)

for question in questions:
    print(f"Question: {question['question']['text']}")
    print(f"Correct Answer: {question['correctAnswer']}")
    print(f"Incorrect Answers: {', '.join(question['incorrectAnswers'])}")
    print()
```

### get_categories
Get a list of categories from the Trivia API.

#### Parameters
- None

#### Returns
A list of categories.

#### Example
```Python
from the_trivia_api_library import TriviaAPIClient

api_key = "YOUR_API_KEY"
client = TriviaAPIClient(api_key=api_key)

tags = client.get_all_tags()

for tag in tags:
    print(tag)
```


### get_totals_per_tag
Get the total number of questions per tag from the Trivia API.

#### Parameters
- `categories` - A list of categories to filter the questions by. Defaults to None.
- `difficulties` - A list of difficulties to filter the questions by. Defaults to None.
- `region` - A list of regions to filter the questions by. Defaults to None.
- `tags` - A list of tags to filter the questions by. Defaults to None.
- `types` - A list of types to filter the questions by. Defaults to None.

#### Returns
A list of totals per tag.

#### Example
```Python
from the_trivia_api_library import TriviaAPIClient

api_key = "YOUR_API_KEY" #it's not necessary
client = TriviaAPIClient(api_key=api_key)

tags = client.get_totals_per_tag()

for tag in tags:
    print(f"tag: {tag} -> total: {tags[tag]}")

```

# Initialize the Trivia API client


## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute to the library, please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This library is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
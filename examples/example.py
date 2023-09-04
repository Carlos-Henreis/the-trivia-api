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
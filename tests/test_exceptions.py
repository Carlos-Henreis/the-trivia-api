from the_trivia_api_library.excepts import TriviaAPIException, InvalidTriviaCategoryError, InvalidTriviaOrderError, InvalidTriviaDifficultyError, InvalidTriviaTypeError

class TestTriviaAPIException:
    """Test TriviaAPIException class."""

    def test_init(self):
        """Test TriviaAPIException constructor."""

        # test with parameters
        trivia_api_exception = TriviaAPIException('test')
        assert trivia_api_exception.args == ('test',)
        assert trivia_api_exception.__str__() == 'test'

class TestInvalidTriviaCategoryError:
    """Test InvalidTriviaCategoryError class."""

    def test_init(self):
        """Test InvalidTriviaCategoryError constructor."""

        # test with parameters
        invalid_trivia_category_error = InvalidTriviaCategoryError('test')
        assert invalid_trivia_category_error.args == ('Invalid trivia category: test',)
        assert invalid_trivia_category_error.__str__() == 'Invalid trivia category: test'

class TestInvalidTriviaOrderError:

    def test_init(self):
        """Test InvalidTriviaOrderError constructor."""

        # test with parameters
        invalid_trivia_order_error = InvalidTriviaOrderError('test')
        assert invalid_trivia_order_error.args == ('Invalid order: test',)
        assert invalid_trivia_order_error.__str__() == 'Invalid order: test'

class TestInvalidTriviaDifficultyError:

        def test_init(self):
            """Test InvalidTriviaDifficultyError constructor."""

            # test with parameters
            invalid_trivia_difficulty_error = InvalidTriviaDifficultyError('test')
            assert invalid_trivia_difficulty_error.args == ('Invalid difficulty: test',)
            assert invalid_trivia_difficulty_error.__str__() == 'Invalid difficulty: test'

class TestInvalidTriviaTypeError:

            def test_init(self):
                """Test InvalidTriviaTypeError constructor."""

                # test with parameters
                invalid_trivia_type_error = InvalidTriviaTypeError('test')
                assert invalid_trivia_type_error.args == ('Invalid type: test',)
                assert invalid_trivia_type_error.__str__() == 'Invalid type: test'
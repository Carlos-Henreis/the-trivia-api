import pytest
from the_trivia_api_library.enums.enum_order import EnumOrder
from the_trivia_api_library.order import TriviaOrder
from the_trivia_api_library.excepts import InvalidTriviaOrderError


class TestTriviaOrder:
    """Test TriviaOrder class."""

    def test_init(self):
        """Test TriviaOrder constructor."""

        # test with no order
        trivia_order = TriviaOrder()
        assert trivia_order._order == EnumOrder.NEW.value

        # test with valid order
        trivia_order = TriviaOrder(EnumOrder.OLD.value)
        assert trivia_order._order == EnumOrder.OLD.value

        # test with invalid order
        with pytest.raises(InvalidTriviaOrderError):
            trivia_order = TriviaOrder('invalid_order')

    def test_set_order(self):
        """Test set_order method."""

        # test with valid order
        trivia_order = TriviaOrder()
        trivia_order.set_order(EnumOrder.OLD.value)
        assert trivia_order._order == EnumOrder.OLD.value

        # test with invalid order
        with pytest.raises(InvalidTriviaOrderError):
            trivia_order.set_order('invalid_order')

    def test_to_query_string(self):
        """Test to_query_string method."""

        # test with no order
        trivia_order = TriviaOrder()
        assert trivia_order.to_query_string() is 'new'

        # test with valid order
        trivia_order = TriviaOrder(EnumOrder.OLD.value)
        assert trivia_order.to_query_string() == EnumOrder.OLD.value
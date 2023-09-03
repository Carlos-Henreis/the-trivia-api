from .enums.enum_order import EnumOrder
from .excepts import InvalidTriviaOrderError

class TriviaOrder:
    """"""

    _order = None
    def __init__(self, order=None):
        """
        TriviaOrder constructor.
        :param order: order
        :return: TriviaOrder object
        """
        if order is None:
            self._order = EnumOrder.NEW.value
        else:
            enum_values = {member.value for member in EnumOrder}
            if (order not in enum_values):
                raise InvalidTriviaOrderError(order)

        self._order = order or EnumOrder.NEW.value

    def set_order(self, order):
        """
        Set the order.
        :param order: order
        :return: None
        """
        enum_values = {member.value for member in EnumOrder}
        if (order in enum_values):
            self._order = order
        else:
            raise InvalidTriviaOrderError(order)

    def to_query_string(self):
        """
        Convert the order to a query string.
        :param: None
        :return: query string
        """
        return self._order or None
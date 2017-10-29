# coding: utf-8

"""
    APITUDE BOOKINGAPI

    BOOKINGAPI is designed to book hotels in real time as fast as in two steps. It covers the complete booking process; it allows generating lists of hotels, confirming bookings, getting lists of bookings, obtaining booking information, making cancellations and modify existing bookings.   BOOKINGAPI works in combination with CONTENTAPI to obtain content information from the hotels, such as pictures, description, facilities, services, etc. Please refer to the ContentAPI documentation and IO/DOCS for related information.    BOOKINGAPI has been designed for a two steps confirmation, but due the the complexity of client and providers systems a third method has been designed.

    OpenAPI spec version: 1.0
    Contact: apitude@hotelbeds.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApiShiftRate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rate_key': 'str',
        'rate_class': 'str',
        'rate_type': 'str',
        'net': 'float',
        'discount': 'float',
        'discount_pct': 'float',
        'selling_rate': 'float',
        'hotel_selling_rate': 'float',
        'amount': 'float',
        'hotel_currency': 'str',
        'hotel_mandatory': 'bool',
        'allotment': 'int',
        'commission': 'float',
        'commission_vat': 'float',
        'commission_pct': 'float',
        'cost': 'ApiCost',
        'check_in': 'date',
        'check_out': 'date'
    }

    attribute_map = {
        'rate_key': 'rateKey',
        'rate_class': 'rateClass',
        'rate_type': 'rateType',
        'net': 'net',
        'discount': 'discount',
        'discount_pct': 'discountPCT',
        'selling_rate': 'sellingRate',
        'hotel_selling_rate': 'hotelSellingRate',
        'amount': 'amount',
        'hotel_currency': 'hotelCurrency',
        'hotel_mandatory': 'hotelMandatory',
        'allotment': 'allotment',
        'commission': 'commission',
        'commission_vat': 'commissionVAT',
        'commission_pct': 'commissionPCT',
        'cost': 'cost',
        'check_in': 'checkIn',
        'check_out': 'checkOut'
    }

    def __init__(self, rate_key=None, rate_class=None, rate_type=None, net=None, discount=None, discount_pct=None, selling_rate=None, hotel_selling_rate=None, amount=None, hotel_currency=None, hotel_mandatory=False, allotment=None, commission=None, commission_vat=None, commission_pct=None, cost=None, check_in=None, check_out=None):
        """
        ApiShiftRate - a model defined in Swagger
        """

        self._rate_key = None
        self._rate_class = None
        self._rate_type = None
        self._net = None
        self._discount = None
        self._discount_pct = None
        self._selling_rate = None
        self._hotel_selling_rate = None
        self._amount = None
        self._hotel_currency = None
        self._hotel_mandatory = None
        self._allotment = None
        self._commission = None
        self._commission_vat = None
        self._commission_pct = None
        self._cost = None
        self._check_in = None
        self._check_out = None

        if rate_key is not None:
          self.rate_key = rate_key
        if rate_class is not None:
          self.rate_class = rate_class
        if rate_type is not None:
          self.rate_type = rate_type
        if net is not None:
          self.net = net
        if discount is not None:
          self.discount = discount
        if discount_pct is not None:
          self.discount_pct = discount_pct
        if selling_rate is not None:
          self.selling_rate = selling_rate
        if hotel_selling_rate is not None:
          self.hotel_selling_rate = hotel_selling_rate
        if amount is not None:
          self.amount = amount
        if hotel_currency is not None:
          self.hotel_currency = hotel_currency
        if hotel_mandatory is not None:
          self.hotel_mandatory = hotel_mandatory
        if allotment is not None:
          self.allotment = allotment
        if commission is not None:
          self.commission = commission
        if commission_vat is not None:
          self.commission_vat = commission_vat
        if commission_pct is not None:
          self.commission_pct = commission_pct
        if cost is not None:
          self.cost = cost
        if check_in is not None:
          self.check_in = check_in
        if check_out is not None:
          self.check_out = check_out

    @property
    def rate_key(self):
        """
        Gets the rate_key of this ApiShiftRate.

        :return: The rate_key of this ApiShiftRate.
        :rtype: str
        """
        return self._rate_key

    @rate_key.setter
    def rate_key(self, rate_key):
        """
        Sets the rate_key of this ApiShiftRate.

        :param rate_key: The rate_key of this ApiShiftRate.
        :type: str
        """

        self._rate_key = rate_key

    @property
    def rate_class(self):
        """
        Gets the rate_class of this ApiShiftRate.

        :return: The rate_class of this ApiShiftRate.
        :rtype: str
        """
        return self._rate_class

    @rate_class.setter
    def rate_class(self, rate_class):
        """
        Sets the rate_class of this ApiShiftRate.

        :param rate_class: The rate_class of this ApiShiftRate.
        :type: str
        """

        self._rate_class = rate_class

    @property
    def rate_type(self):
        """
        Gets the rate_type of this ApiShiftRate.

        :return: The rate_type of this ApiShiftRate.
        :rtype: str
        """
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        """
        Sets the rate_type of this ApiShiftRate.

        :param rate_type: The rate_type of this ApiShiftRate.
        :type: str
        """
        allowed_values = ["BOOKABLE", "RECHECK"]
        if rate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `rate_type` ({0}), must be one of {1}"
                .format(rate_type, allowed_values)
            )

        self._rate_type = rate_type

    @property
    def net(self):
        """
        Gets the net of this ApiShiftRate.

        :return: The net of this ApiShiftRate.
        :rtype: float
        """
        return self._net

    @net.setter
    def net(self, net):
        """
        Sets the net of this ApiShiftRate.

        :param net: The net of this ApiShiftRate.
        :type: float
        """

        self._net = net

    @property
    def discount(self):
        """
        Gets the discount of this ApiShiftRate.

        :return: The discount of this ApiShiftRate.
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """
        Sets the discount of this ApiShiftRate.

        :param discount: The discount of this ApiShiftRate.
        :type: float
        """

        self._discount = discount

    @property
    def discount_pct(self):
        """
        Gets the discount_pct of this ApiShiftRate.

        :return: The discount_pct of this ApiShiftRate.
        :rtype: float
        """
        return self._discount_pct

    @discount_pct.setter
    def discount_pct(self, discount_pct):
        """
        Sets the discount_pct of this ApiShiftRate.

        :param discount_pct: The discount_pct of this ApiShiftRate.
        :type: float
        """

        self._discount_pct = discount_pct

    @property
    def selling_rate(self):
        """
        Gets the selling_rate of this ApiShiftRate.

        :return: The selling_rate of this ApiShiftRate.
        :rtype: float
        """
        return self._selling_rate

    @selling_rate.setter
    def selling_rate(self, selling_rate):
        """
        Sets the selling_rate of this ApiShiftRate.

        :param selling_rate: The selling_rate of this ApiShiftRate.
        :type: float
        """

        self._selling_rate = selling_rate

    @property
    def hotel_selling_rate(self):
        """
        Gets the hotel_selling_rate of this ApiShiftRate.

        :return: The hotel_selling_rate of this ApiShiftRate.
        :rtype: float
        """
        return self._hotel_selling_rate

    @hotel_selling_rate.setter
    def hotel_selling_rate(self, hotel_selling_rate):
        """
        Sets the hotel_selling_rate of this ApiShiftRate.

        :param hotel_selling_rate: The hotel_selling_rate of this ApiShiftRate.
        :type: float
        """

        self._hotel_selling_rate = hotel_selling_rate

    @property
    def amount(self):
        """
        Gets the amount of this ApiShiftRate.

        :return: The amount of this ApiShiftRate.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this ApiShiftRate.

        :param amount: The amount of this ApiShiftRate.
        :type: float
        """

        self._amount = amount

    @property
    def hotel_currency(self):
        """
        Gets the hotel_currency of this ApiShiftRate.

        :return: The hotel_currency of this ApiShiftRate.
        :rtype: str
        """
        return self._hotel_currency

    @hotel_currency.setter
    def hotel_currency(self, hotel_currency):
        """
        Sets the hotel_currency of this ApiShiftRate.

        :param hotel_currency: The hotel_currency of this ApiShiftRate.
        :type: str
        """

        self._hotel_currency = hotel_currency

    @property
    def hotel_mandatory(self):
        """
        Gets the hotel_mandatory of this ApiShiftRate.

        :return: The hotel_mandatory of this ApiShiftRate.
        :rtype: bool
        """
        return self._hotel_mandatory

    @hotel_mandatory.setter
    def hotel_mandatory(self, hotel_mandatory):
        """
        Sets the hotel_mandatory of this ApiShiftRate.

        :param hotel_mandatory: The hotel_mandatory of this ApiShiftRate.
        :type: bool
        """

        self._hotel_mandatory = hotel_mandatory

    @property
    def allotment(self):
        """
        Gets the allotment of this ApiShiftRate.

        :return: The allotment of this ApiShiftRate.
        :rtype: int
        """
        return self._allotment

    @allotment.setter
    def allotment(self, allotment):
        """
        Sets the allotment of this ApiShiftRate.

        :param allotment: The allotment of this ApiShiftRate.
        :type: int
        """

        self._allotment = allotment

    @property
    def commission(self):
        """
        Gets the commission of this ApiShiftRate.

        :return: The commission of this ApiShiftRate.
        :rtype: float
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """
        Sets the commission of this ApiShiftRate.

        :param commission: The commission of this ApiShiftRate.
        :type: float
        """

        self._commission = commission

    @property
    def commission_vat(self):
        """
        Gets the commission_vat of this ApiShiftRate.

        :return: The commission_vat of this ApiShiftRate.
        :rtype: float
        """
        return self._commission_vat

    @commission_vat.setter
    def commission_vat(self, commission_vat):
        """
        Sets the commission_vat of this ApiShiftRate.

        :param commission_vat: The commission_vat of this ApiShiftRate.
        :type: float
        """

        self._commission_vat = commission_vat

    @property
    def commission_pct(self):
        """
        Gets the commission_pct of this ApiShiftRate.

        :return: The commission_pct of this ApiShiftRate.
        :rtype: float
        """
        return self._commission_pct

    @commission_pct.setter
    def commission_pct(self, commission_pct):
        """
        Sets the commission_pct of this ApiShiftRate.

        :param commission_pct: The commission_pct of this ApiShiftRate.
        :type: float
        """

        self._commission_pct = commission_pct

    @property
    def cost(self):
        """
        Gets the cost of this ApiShiftRate.

        :return: The cost of this ApiShiftRate.
        :rtype: ApiCost
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this ApiShiftRate.

        :param cost: The cost of this ApiShiftRate.
        :type: ApiCost
        """

        self._cost = cost

    @property
    def check_in(self):
        """
        Gets the check_in of this ApiShiftRate.

        :return: The check_in of this ApiShiftRate.
        :rtype: date
        """
        return self._check_in

    @check_in.setter
    def check_in(self, check_in):
        """
        Sets the check_in of this ApiShiftRate.

        :param check_in: The check_in of this ApiShiftRate.
        :type: date
        """

        self._check_in = check_in

    @property
    def check_out(self):
        """
        Gets the check_out of this ApiShiftRate.

        :return: The check_out of this ApiShiftRate.
        :rtype: date
        """
        return self._check_out

    @check_out.setter
    def check_out(self, check_out):
        """
        Sets the check_out of this ApiShiftRate.

        :param check_out: The check_out of this ApiShiftRate.
        :type: date
        """

        self._check_out = check_out

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ApiShiftRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
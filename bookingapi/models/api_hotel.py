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


class ApiHotel(object):
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
        'check_out': 'date',
        'check_in': 'date',
        'code': 'int',
        'name': 'str',
        'description': 'str',
        'image': 'str',
        'category_code': 'str',
        'category_name': 'str',
        'destination_code': 'str',
        'destination_name': 'str',
        'zone_code': 'int',
        'zone_name': 'str',
        'latitude': 'str',
        'longitude': 'str',
        'giata': 'str',
        'min_rate': 'float',
        'max_rate': 'float',
        'total_selling_rate': 'float',
        'total_net': 'float',
        'pending_amount': 'float',
        'currency': 'str',
        'supplier': 'ApiSupplier',
        'client_comments': 'str',
        'cancellation_amount': 'float',
        'upselling': 'ApiUpselling',
        'keyword': 'list[ApiKeyword]',
        'review': 'list[ApiReview]',
        'rooms': 'list[Room]',
        'credit_card': 'list[ApiCreditCard]'
    }

    attribute_map = {
        'check_out': 'checkOut',
        'check_in': 'checkIn',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'image': 'image',
        'category_code': 'categoryCode',
        'category_name': 'categoryName',
        'destination_code': 'destinationCode',
        'destination_name': 'destinationName',
        'zone_code': 'zoneCode',
        'zone_name': 'zoneName',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'giata': 'giata',
        'min_rate': 'minRate',
        'max_rate': 'maxRate',
        'total_selling_rate': 'totalSellingRate',
        'total_net': 'totalNet',
        'pending_amount': 'pendingAmount',
        'currency': 'currency',
        'supplier': 'supplier',
        'client_comments': 'clientComments',
        'cancellation_amount': 'cancellationAmount',
        'upselling': 'upselling',
        'keyword': 'keyword',
        'review': 'review',
        'rooms': 'rooms',
        'credit_card': 'creditCard'
    }

    def __init__(self, check_out=None, check_in=None, code=None, name=None, description=None, image=None, category_code=None, category_name=None, destination_code=None, destination_name=None, zone_code=None, zone_name=None, latitude=None, longitude=None, giata=None, min_rate=None, max_rate=None, total_selling_rate=None, total_net=None, pending_amount=None, currency=None, supplier=None, client_comments=None, cancellation_amount=None, upselling=None, keyword=None, review=None, room=None, credit_card=None):
        """
        ApiHotel - a model defined in Swagger
        """

        self._check_out = None
        self._check_in = None
        self._code = None
        self._name = None
        self._description = None
        self._image = None
        self._category_code = None
        self._category_name = None
        self._destination_code = None
        self._destination_name = None
        self._zone_code = None
        self._zone_name = None
        self._latitude = None
        self._longitude = None
        self._giata = None
        self._min_rate = None
        self._max_rate = None
        self._total_selling_rate = None
        self._total_net = None
        self._pending_amount = None
        self._currency = None
        self._supplier = None
        self._client_comments = None
        self._cancellation_amount = None
        self._upselling = None
        self._keyword = None
        self._review = None
        self._rooms = None
        self._credit_card = None

        if check_out is not None:
          self.check_out = check_out
        if check_in is not None:
          self.check_in = check_in
        if code is not None:
          self.code = code
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if image is not None:
          self.image = image
        if category_code is not None:
          self.category_code = category_code
        if category_name is not None:
          self.category_name = category_name
        if destination_code is not None:
          self.destination_code = destination_code
        if destination_name is not None:
          self.destination_name = destination_name
        if zone_code is not None:
          self.zone_code = zone_code
        if zone_name is not None:
          self.zone_name = zone_name
        if latitude is not None:
          self.latitude = latitude
        if longitude is not None:
          self.longitude = longitude
        if giata is not None:
          self.giata = giata
        if min_rate is not None:
          self.min_rate = min_rate
        if max_rate is not None:
          self.max_rate = max_rate
        if total_selling_rate is not None:
          self.total_selling_rate = total_selling_rate
        if total_net is not None:
          self.total_net = total_net
        if pending_amount is not None:
          self.pending_amount = pending_amount
        if currency is not None:
          self.currency = currency
        if supplier is not None:
          self.supplier = supplier
        if client_comments is not None:
          self.client_comments = client_comments
        if cancellation_amount is not None:
          self.cancellation_amount = cancellation_amount
        if upselling is not None:
          self.upselling = upselling
        if keyword is not None:
          self.keyword = keyword
        if review is not None:
          self.review = review
        if rooms is not None:
          self.rooms = rooms
        if credit_card is not None:
          self.credit_card = credit_card

    @property
    def check_out(self):
        """
        Gets the check_out of this ApiHotel.

        :return: The check_out of this ApiHotel.
        :rtype: date
        """
        return self._check_out

    @check_out.setter
    def check_out(self, check_out):
        """
        Sets the check_out of this ApiHotel.

        :param check_out: The check_out of this ApiHotel.
        :type: date
        """

        self._check_out = check_out

    @property
    def check_in(self):
        """
        Gets the check_in of this ApiHotel.

        :return: The check_in of this ApiHotel.
        :rtype: date
        """
        return self._check_in

    @check_in.setter
    def check_in(self, check_in):
        """
        Sets the check_in of this ApiHotel.

        :param check_in: The check_in of this ApiHotel.
        :type: date
        """

        self._check_in = check_in

    @property
    def code(self):
        """
        Gets the code of this ApiHotel.

        :return: The code of this ApiHotel.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ApiHotel.

        :param code: The code of this ApiHotel.
        :type: int
        """

        self._code = code

    @property
    def name(self):
        """
        Gets the name of this ApiHotel.

        :return: The name of this ApiHotel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApiHotel.

        :param name: The name of this ApiHotel.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ApiHotel.

        :return: The description of this ApiHotel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ApiHotel.

        :param description: The description of this ApiHotel.
        :type: str
        """

        self._description = description

    @property
    def image(self):
        """
        Gets the image of this ApiHotel.

        :return: The image of this ApiHotel.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this ApiHotel.

        :param image: The image of this ApiHotel.
        :type: str
        """

        self._image = image

    @property
    def category_code(self):
        """
        Gets the category_code of this ApiHotel.

        :return: The category_code of this ApiHotel.
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """
        Sets the category_code of this ApiHotel.

        :param category_code: The category_code of this ApiHotel.
        :type: str
        """

        self._category_code = category_code

    @property
    def category_name(self):
        """
        Gets the category_name of this ApiHotel.

        :return: The category_name of this ApiHotel.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """
        Sets the category_name of this ApiHotel.

        :param category_name: The category_name of this ApiHotel.
        :type: str
        """

        self._category_name = category_name

    @property
    def destination_code(self):
        """
        Gets the destination_code of this ApiHotel.

        :return: The destination_code of this ApiHotel.
        :rtype: str
        """
        return self._destination_code

    @destination_code.setter
    def destination_code(self, destination_code):
        """
        Sets the destination_code of this ApiHotel.

        :param destination_code: The destination_code of this ApiHotel.
        :type: str
        """

        self._destination_code = destination_code

    @property
    def destination_name(self):
        """
        Gets the destination_name of this ApiHotel.

        :return: The destination_name of this ApiHotel.
        :rtype: str
        """
        return self._destination_name

    @destination_name.setter
    def destination_name(self, destination_name):
        """
        Sets the destination_name of this ApiHotel.

        :param destination_name: The destination_name of this ApiHotel.
        :type: str
        """

        self._destination_name = destination_name

    @property
    def zone_code(self):
        """
        Gets the zone_code of this ApiHotel.

        :return: The zone_code of this ApiHotel.
        :rtype: int
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        """
        Sets the zone_code of this ApiHotel.

        :param zone_code: The zone_code of this ApiHotel.
        :type: int
        """

        self._zone_code = zone_code

    @property
    def zone_name(self):
        """
        Gets the zone_name of this ApiHotel.

        :return: The zone_name of this ApiHotel.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """
        Sets the zone_name of this ApiHotel.

        :param zone_name: The zone_name of this ApiHotel.
        :type: str
        """

        self._zone_name = zone_name

    @property
    def latitude(self):
        """
        Gets the latitude of this ApiHotel.

        :return: The latitude of this ApiHotel.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this ApiHotel.

        :param latitude: The latitude of this ApiHotel.
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this ApiHotel.

        :return: The longitude of this ApiHotel.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this ApiHotel.

        :param longitude: The longitude of this ApiHotel.
        :type: str
        """

        self._longitude = longitude

    @property
    def giata(self):
        """
        Gets the giata of this ApiHotel.

        :return: The giata of this ApiHotel.
        :rtype: str
        """
        return self._giata

    @giata.setter
    def giata(self, giata):
        """
        Sets the giata of this ApiHotel.

        :param giata: The giata of this ApiHotel.
        :type: str
        """

        self._giata = giata

    @property
    def min_rate(self):
        """
        Gets the min_rate of this ApiHotel.

        :return: The min_rate of this ApiHotel.
        :rtype: float
        """
        return self._min_rate

    @min_rate.setter
    def min_rate(self, min_rate):
        """
        Sets the min_rate of this ApiHotel.

        :param min_rate: The min_rate of this ApiHotel.
        :type: float
        """

        self._min_rate = min_rate

    @property
    def max_rate(self):
        """
        Gets the max_rate of this ApiHotel.

        :return: The max_rate of this ApiHotel.
        :rtype: float
        """
        return self._max_rate

    @max_rate.setter
    def max_rate(self, max_rate):
        """
        Sets the max_rate of this ApiHotel.

        :param max_rate: The max_rate of this ApiHotel.
        :type: float
        """

        self._max_rate = max_rate

    @property
    def total_selling_rate(self):
        """
        Gets the total_selling_rate of this ApiHotel.

        :return: The total_selling_rate of this ApiHotel.
        :rtype: float
        """
        return self._total_selling_rate

    @total_selling_rate.setter
    def total_selling_rate(self, total_selling_rate):
        """
        Sets the total_selling_rate of this ApiHotel.

        :param total_selling_rate: The total_selling_rate of this ApiHotel.
        :type: float
        """

        self._total_selling_rate = total_selling_rate

    @property
    def total_net(self):
        """
        Gets the total_net of this ApiHotel.

        :return: The total_net of this ApiHotel.
        :rtype: float
        """
        return self._total_net

    @total_net.setter
    def total_net(self, total_net):
        """
        Sets the total_net of this ApiHotel.

        :param total_net: The total_net of this ApiHotel.
        :type: float
        """

        self._total_net = total_net

    @property
    def pending_amount(self):
        """
        Gets the pending_amount of this ApiHotel.

        :return: The pending_amount of this ApiHotel.
        :rtype: float
        """
        return self._pending_amount

    @pending_amount.setter
    def pending_amount(self, pending_amount):
        """
        Sets the pending_amount of this ApiHotel.

        :param pending_amount: The pending_amount of this ApiHotel.
        :type: float
        """

        self._pending_amount = pending_amount

    @property
    def currency(self):
        """
        Gets the currency of this ApiHotel.

        :return: The currency of this ApiHotel.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this ApiHotel.

        :param currency: The currency of this ApiHotel.
        :type: str
        """

        self._currency = currency

    @property
    def supplier(self):
        """
        Gets the supplier of this ApiHotel.

        :return: The supplier of this ApiHotel.
        :rtype: ApiSupplier
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """
        Sets the supplier of this ApiHotel.

        :param supplier: The supplier of this ApiHotel.
        :type: ApiSupplier
        """

        self._supplier = supplier

    @property
    def client_comments(self):
        """
        Gets the client_comments of this ApiHotel.

        :return: The client_comments of this ApiHotel.
        :rtype: str
        """
        return self._client_comments

    @client_comments.setter
    def client_comments(self, client_comments):
        """
        Sets the client_comments of this ApiHotel.

        :param client_comments: The client_comments of this ApiHotel.
        :type: str
        """

        self._client_comments = client_comments

    @property
    def cancellation_amount(self):
        """
        Gets the cancellation_amount of this ApiHotel.

        :return: The cancellation_amount of this ApiHotel.
        :rtype: float
        """
        return self._cancellation_amount

    @cancellation_amount.setter
    def cancellation_amount(self, cancellation_amount):
        """
        Sets the cancellation_amount of this ApiHotel.

        :param cancellation_amount: The cancellation_amount of this ApiHotel.
        :type: float
        """

        self._cancellation_amount = cancellation_amount

    @property
    def upselling(self):
        """
        Gets the upselling of this ApiHotel.

        :return: The upselling of this ApiHotel.
        :rtype: ApiUpselling
        """
        return self._upselling

    @upselling.setter
    def upselling(self, upselling):
        """
        Sets the upselling of this ApiHotel.

        :param upselling: The upselling of this ApiHotel.
        :type: ApiUpselling
        """

        self._upselling = upselling

    @property
    def keyword(self):
        """
        Gets the keyword of this ApiHotel.

        :return: The keyword of this ApiHotel.
        :rtype: list[ApiKeyword]
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """
        Sets the keyword of this ApiHotel.

        :param keyword: The keyword of this ApiHotel.
        :type: list[ApiKeyword]
        """

        self._keyword = keyword

    @property
    def review(self):
        """
        Gets the review of this ApiHotel.

        :return: The review of this ApiHotel.
        :rtype: list[ApiReview]
        """
        return self._review

    @review.setter
    def review(self, review):
        """
        Sets the review of this ApiHotel.

        :param review: The review of this ApiHotel.
        :type: list[ApiReview]
        """

        self._review = review

    @property
    def rooms(self):
        """
        Gets the rooms of this ApiHotel.

        :return: The rooms of this ApiHotel.
        :rtype: list[Room]
        """
        return self._room

    @rooms.setter
    def rooms(self, rooms):
        """
        Sets the rooms of this ApiHotel.

        :param rooms: The rooms of this ApiHotel.
        :type: list[Room]
        """

        self._rooms = rooms

    @property
    def credit_card(self):
        """
        Gets the credit_card of this ApiHotel.

        :return: The credit_card of this ApiHotel.
        :rtype: list[ApiCreditCard]
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """
        Sets the credit_card of this ApiHotel.

        :param credit_card: The credit_card of this ApiHotel.
        :type: list[ApiCreditCard]
        """

        self._credit_card = credit_card

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
        if not isinstance(other, ApiHotel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

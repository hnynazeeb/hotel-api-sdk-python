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


class BookingRS(object):
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
        'echo_token': 'str',
        'audit_data': 'ApiAuditData',
        'error': 'ApiError',
        'source': 'ApiSource',
        'booking': 'ApiBooking'
    }

    attribute_map = {
        'echo_token': 'echoToken',
        'audit_data': 'auditData',
        'error': 'error',
        'source': 'source',
        'booking': 'booking'
    }

    def __init__(self, echo_token=None, audit_data=None, error=None, source=None, booking=None):
        """
        BookingRS - a model defined in Swagger
        """

        self._echo_token = None
        self._audit_data = None
        self._error = None
        self._source = None
        self._booking = None

        if echo_token is not None:
          self.echo_token = echo_token
        self.audit_data = audit_data
        if error is not None:
          self.error = error
        if source is not None:
          self.source = source
        if booking is not None:
          self.booking = booking

    @property
    def echo_token(self):
        """
        Gets the echo_token of this BookingRS.

        :return: The echo_token of this BookingRS.
        :rtype: str
        """
        return self._echo_token

    @echo_token.setter
    def echo_token(self, echo_token):
        """
        Sets the echo_token of this BookingRS.

        :param echo_token: The echo_token of this BookingRS.
        :type: str
        """

        self._echo_token = echo_token

    @property
    def audit_data(self):
        """
        Gets the audit_data of this BookingRS.

        :return: The audit_data of this BookingRS.
        :rtype: ApiAuditData
        """
        return self._audit_data

    @audit_data.setter
    def audit_data(self, audit_data):
        """
        Sets the audit_data of this BookingRS.

        :param audit_data: The audit_data of this BookingRS.
        :type: ApiAuditData
        """
        if audit_data is None:
            raise ValueError("Invalid value for `audit_data`, must not be `None`")

        self._audit_data = audit_data

    @property
    def error(self):
        """
        Gets the error of this BookingRS.

        :return: The error of this BookingRS.
        :rtype: ApiError
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this BookingRS.

        :param error: The error of this BookingRS.
        :type: ApiError
        """

        self._error = error

    @property
    def source(self):
        """
        Gets the source of this BookingRS.

        :return: The source of this BookingRS.
        :rtype: ApiSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this BookingRS.

        :param source: The source of this BookingRS.
        :type: ApiSource
        """

        self._source = source

    @property
    def booking(self):
        """
        Gets the booking of this BookingRS.

        :return: The booking of this BookingRS.
        :rtype: ApiBooking
        """
        return self._booking

    @booking.setter
    def booking(self, booking):
        """
        Sets the booking of this BookingRS.

        :param booking: The booking of this BookingRS.
        :type: ApiBooking
        """

        self._booking = booking

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
        if not isinstance(other, BookingRS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

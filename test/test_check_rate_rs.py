# coding: utf-8

"""
    APITUDE BOOKINGAPI

    BOOKINGAPI is designed to book hotels in real time as fast as in two steps. It covers the complete booking process; it allows generating lists of hotels, confirming bookings, getting lists of bookings, obtaining booking information, making cancellations and modify existing bookings.   BOOKINGAPI works in combination with CONTENTAPI to obtain content information from the hotels, such as pictures, description, facilities, services, etc. Please refer to the ContentAPI documentation and IO/DOCS for related information.    BOOKINGAPI has been designed for a two steps confirmation, but due the the complexity of client and providers systems a third method has been designed.

    OpenAPI spec version: 1.0
    Contact: apitude@hotelbeds.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import bookingapi
from bookingapi.rest import ApiException
from bookingapi.models.check_rate_rs import CheckRateRS


class TestCheckRateRS(unittest.TestCase):
    """ CheckRateRS unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCheckRateRS(self):
        """
        Test CheckRateRS
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = bookingapi.models.check_rate_rs.CheckRateRS()
        pass


if __name__ == '__main__':
    unittest.main()

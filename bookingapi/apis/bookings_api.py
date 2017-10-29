# coding: utf-8

"""
    APITUDE BOOKINGAPI

    BOOKINGAPI is designed to book hotels in real time as fast as in two steps. It covers the complete booking process; it allows generating lists of hotels, confirming bookings, getting lists of bookings, obtaining booking information, making cancellations and modify existing bookings.   BOOKINGAPI works in combination with CONTENTAPI to obtain content information from the hotels, such as pictures, description, facilities, services, etc. Please refer to the ContentAPI documentation and IO/DOCS for related information.    BOOKINGAPI has been designed for a two steps confirmation, but due the the complexity of client and providers systems a third method has been designed.

    OpenAPI spec version: 1.0
    Contact: apitude@hotelbeds.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class BookingsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def booking(self, version, body, **kwargs):
        """
        Booking confirm
        The booking confirmation operation confirms the rate keys selected.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.booking(version, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: Default version for this operation (required)
        :param BookingRQ body: (required)
        :return: BookingRS
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.booking_with_http_info(version, body, **kwargs)
        else:
            (data) = self.booking_with_http_info(version, body, **kwargs)
            return data

    def booking_with_http_info(self, version, body, **kwargs):
        """
        Booking confirm
        The booking confirmation operation confirms the rate keys selected.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.booking_with_http_info(version, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: Default version for this operation (required)
        :param BookingRQ body: (required)
        :return: BookingRS
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method booking" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `booking`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `booking`")


        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/{version}/bookings', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BookingRS',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def booking_cancellation(self, version, booking_id, **kwargs):
        """
        Booking cancellation
        The BookingCancellation operation cancels a booking or simulates a booking cancellation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.booking_cancellation(version, booking_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: Default version for this operation (required)
        :param str booking_id: (required)
        :param str cancellation_flag:
        :param str language:
        :return: BookingCancellationRS
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.booking_cancellation_with_http_info(version, booking_id, **kwargs)
        else:
            (data) = self.booking_cancellation_with_http_info(version, booking_id, **kwargs)
            return data

    def booking_cancellation_with_http_info(self, version, booking_id, **kwargs):
        """
        Booking cancellation
        The BookingCancellation operation cancels a booking or simulates a booking cancellation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.booking_cancellation_with_http_info(version, booking_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: Default version for this operation (required)
        :param str booking_id: (required)
        :param str cancellation_flag:
        :param str language:
        :return: BookingCancellationRS
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'booking_id', 'cancellation_flag', 'language']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method booking_cancellation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `booking_cancellation`")
        # verify the required parameter 'booking_id' is set
        if ('booking_id' not in params) or (params['booking_id'] is None):
            raise ValueError("Missing the required parameter `booking_id` when calling `booking_cancellation`")


        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']
        if 'booking_id' in params:
            path_params['bookingId'] = params['booking_id']

        query_params = []
        if 'cancellation_flag' in params:
            query_params.append(('cancellationFlag', params['cancellation_flag']))
        if 'language' in params:
            query_params.append(('language', params['language']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/{version}/bookings/{bookingId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BookingCancellationRS',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def booking_change(self, version, booking_id, body, **kwargs):
        """
        Booking change
        The BookingChange operation can be used to change (or simulate) different values of a booking or to partially cancel a booking (i.e: cancel a room of a two room reservation).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.booking_change(version, booking_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: Default version for this operation (required)
        :param str booking_id: (required)
        :param BookingChangeRQ body: (required)
        :return: BookingChangeRS
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.booking_change_with_http_info(version, booking_id, body, **kwargs)
        else:
            (data) = self.booking_change_with_http_info(version, booking_id, body, **kwargs)
            return data

    def booking_change_with_http_info(self, version, booking_id, body, **kwargs):
        """
        Booking change
        The BookingChange operation can be used to change (or simulate) different values of a booking or to partially cancel a booking (i.e: cancel a room of a two room reservation).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.booking_change_with_http_info(version, booking_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: Default version for this operation (required)
        :param str booking_id: (required)
        :param BookingChangeRQ body: (required)
        :return: BookingChangeRS
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'booking_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method booking_change" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `booking_change`")
        # verify the required parameter 'booking_id' is set
        if ('booking_id' not in params) or (params['booking_id'] is None):
            raise ValueError("Missing the required parameter `booking_id` when calling `booking_change`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `booking_change`")


        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']
        if 'booking_id' in params:
            path_params['bookingId'] = params['booking_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/{version}/bookings/{bookingId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BookingChangeRS',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def booking_detail(self, version, booking_id, **kwargs):
        """
        Booking detail
        The BookingDetail operation retuns all the information of the requested booking.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.booking_detail(version, booking_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: Default version for this operation (required)
        :param str booking_id: (required)
        :param str language:
        :return: BookingDetailRS
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.booking_detail_with_http_info(version, booking_id, **kwargs)
        else:
            (data) = self.booking_detail_with_http_info(version, booking_id, **kwargs)
            return data

    def booking_detail_with_http_info(self, version, booking_id, **kwargs):
        """
        Booking detail
        The BookingDetail operation retuns all the information of the requested booking.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.booking_detail_with_http_info(version, booking_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: Default version for this operation (required)
        :param str booking_id: (required)
        :param str language:
        :return: BookingDetailRS
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'booking_id', 'language']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method booking_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `booking_detail`")
        # verify the required parameter 'booking_id' is set
        if ('booking_id' not in params) or (params['booking_id'] is None):
            raise ValueError("Missing the required parameter `booking_id` when calling `booking_detail`")


        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']
        if 'booking_id' in params:
            path_params['bookingId'] = params['booking_id']

        query_params = []
        if 'language' in params:
            query_params.append(('language', params['language']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/{version}/bookings/{bookingId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BookingDetailRS',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

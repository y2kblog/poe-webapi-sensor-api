# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.rms_result import RmsResult  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRmsController(BaseTestCase):
    """RmsController integration test stubs"""

    def test_get_rms(self):
        """Test case for get_rms

        音圧のRMS値を取得
        """
        query_string = [('lowerFrqHz', 10),
                        ('upperFrqHz', 80000),
                        ('timeSec', 0.0256)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/rms',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

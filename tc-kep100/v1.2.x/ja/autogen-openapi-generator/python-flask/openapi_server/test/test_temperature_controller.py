# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.temperature import Temperature  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTemperatureController(BaseTestCase):
    """TemperatureController integration test stubs"""

    def test_temperature_get(self):
        """Test case for temperature_get

        熱電対の温度の取得
        """
        query_string = [('unit', 'unit_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/temperature',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

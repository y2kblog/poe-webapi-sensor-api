# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.sound_level_result import SoundLevelResult  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNoiseController(BaseTestCase):
    """NoiseController integration test stubs"""

    def test_get_noise(self):
        """Test case for get_noise

        騒音レベルの取得 
        """
        query_string = [('timeSec', 0.5),
                        ('timeWeight', 'slow')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/noise',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

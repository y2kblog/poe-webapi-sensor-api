# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestInitController(BaseTestCase):
    """InitController integration test stubs"""

    def test_init_put(self):
        """Test case for init_put

        製品を初期状態に戻す
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/init',
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

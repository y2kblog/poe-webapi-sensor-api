# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.raw_setting import RawSetting  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRawController(BaseTestCase):
    """RawController integration test stubs"""

    def test_raw_delete(self):
        """Test case for raw_delete

        生値取得終了
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/raw',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_raw_post(self):
        """Test case for raw_post

        生値取得開始
        """
        raw_setting = openapi_server.RawSetting()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/raw',
            method='POST',
            headers=headers,
            data=json.dumps(raw_setting),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_raw_status_get(self):
        """Test case for raw_status_get

        生値取得状態の取得
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/raw-status',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

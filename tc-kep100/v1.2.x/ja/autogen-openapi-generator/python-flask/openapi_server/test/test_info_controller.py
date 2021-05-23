# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.info import Info  # noqa: E501
from openapi_server.models.info_configurable import InfoConfigurable  # noqa: E501
from openapi_server.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_info_get(self):
        """Test case for info_get

        機器情報の取得
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/info',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_patch(self):
        """Test case for info_patch

        設定変更が可能な機器情報の変更
        """
        info_configurable = openapi_server.InfoConfigurable()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/info',
            method='PATCH',
            headers=headers,
            data=json.dumps(info_configurable),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

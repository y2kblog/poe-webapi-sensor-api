# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.network_config import NetworkConfig  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNetworkController(BaseTestCase):
    """NetworkController integration test stubs"""

    def test_config_network_get(self):
        """Test case for config_network_get

        ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/config/network',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_config_network_patch(self):
        """Test case for config_network_patch

        ネットワーク設定（認証機能・DHCP・手動IP）の変更
        """
        network_config = openapi_server.NetworkConfig()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/config/network',
            method='PATCH',
            headers=headers,
            data=json.dumps(network_config),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

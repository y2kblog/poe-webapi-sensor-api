# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.alert import Alert  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAlertController(BaseTestCase):
    """AlertController integration test stubs"""

    def test_add_alert_setting(self):
        """Test case for add_alert_setting

        アラート設定を1つ登録
        """
        alert = openapi_server.Alert()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/alerts',
            method='POST',
            headers=headers,
            data=json.dumps(alert),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_alerts_alert_id_delete(self):
        """Test case for alerts_alert_id_delete

        指定したidのアラート設定を削除
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/alerts/{alert_id}'.format(alert_id=0),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_alerts_delete(self):
        """Test case for alerts_delete

        登録済みアラート設定を全て削除
        """
        headers = { 
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/alerts',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_alert_by_id(self):
        """Test case for get_alert_by_id

        指定したidのアラート設定を取得
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/alerts/{alert_id}'.format(alert_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_alerts(self):
        """Test case for get_alerts

        登録済みアラート設定一覧を取得
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/alerts',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

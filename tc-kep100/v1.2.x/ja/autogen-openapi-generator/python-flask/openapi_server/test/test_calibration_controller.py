# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.thermocouple_calib import ThermocoupleCalib  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCalibrationController(BaseTestCase):
    """CalibrationController integration test stubs"""

    def test_calibration_get(self):
        """Test case for calibration_get

        校正パラメータの取得
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/calibration',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_calibration_put(self):
        """Test case for calibration_put

        熱電対の校正を実行
        """
        thermocouple_calib = openapi_server.ThermocoupleCalib()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/calibration',
            method='PUT',
            headers=headers,
            data=json.dumps(thermocouple_calib),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

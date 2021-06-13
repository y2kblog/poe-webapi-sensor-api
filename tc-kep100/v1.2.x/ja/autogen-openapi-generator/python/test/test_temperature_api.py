"""
    PoE対応 WebAPI K型熱電対アンプ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 1.2.x
    Generated by: https://openapi-generator.tech
"""


import unittest

import tc_kep100_client
from tc_kep100_client.api.temperature_api import TemperatureApi  # noqa: E501


class TestTemperatureApi(unittest.TestCase):
    """TemperatureApi unit test stubs"""

    def setUp(self):
        self.api = TemperatureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_temperature_get(self):
        """Test case for temperature_get

        熱電対の温度の取得  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

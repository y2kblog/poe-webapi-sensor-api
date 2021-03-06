"""
    PoE対応 WebAPI 超音波センサ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 2.0.x
    Generated by: https://openapi-generator.tech
"""


import unittest

import mc_uep100_client
from mc_uep100_client.api.rms_api import RmsApi  # noqa: E501


class TestRmsApi(unittest.TestCase):
    """RmsApi unit test stubs"""

    def setUp(self):
        self.api = RmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_rms(self):
        """Test case for get_rms

        音圧のRMS値を取得  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

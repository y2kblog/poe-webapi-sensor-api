"""
    PoE対応 WebAPI 超音波センサ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 2.0.x
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.noise_api import NoiseApi  # noqa: E501


class TestNoiseApi(unittest.TestCase):
    """NoiseApi unit test stubs"""

    def setUp(self):
        self.api = NoiseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_noise(self):
        """Test case for get_noise

        騒音レベルの取得   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

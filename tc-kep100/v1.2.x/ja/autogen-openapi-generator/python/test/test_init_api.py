"""
    PoE対応 WebAPI K型熱電対アンプ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 1.2.x
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.init_api import InitApi  # noqa: E501


class TestInitApi(unittest.TestCase):
    """InitApi unit test stubs"""

    def setUp(self):
        self.api = InitApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_init_put(self):
        """Test case for init_put

        製品を初期状態に戻す  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

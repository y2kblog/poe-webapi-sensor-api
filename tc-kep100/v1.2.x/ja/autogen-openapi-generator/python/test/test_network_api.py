"""
    PoE対応 WebAPI K型熱電対アンプ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 1.2.x
    Generated by: https://openapi-generator.tech
"""


import unittest

import tc_kep100_client
from tc_kep100_client.api.network_api import NetworkApi  # noqa: E501


class TestNetworkApi(unittest.TestCase):
    """NetworkApi unit test stubs"""

    def setUp(self):
        self.api = NetworkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_config_network_get(self):
        """Test case for config_network_get

        ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得  # noqa: E501
        """
        pass

    def test_config_network_patch(self):
        """Test case for config_network_patch

        ネットワーク設定（認証機能・DHCP・手動IP）の変更  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

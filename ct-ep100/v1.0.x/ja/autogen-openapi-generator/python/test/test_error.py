"""
    PoE対応 WebAPI CO2センサ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 1.0.x
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ct_ep100_client
from ct_ep100_client.model.error_error import ErrorError
globals()['ErrorError'] = ErrorError
from ct_ep100_client.model.error import Error


class TestError(unittest.TestCase):
    """Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testError(self):
        """Test Error"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Error()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

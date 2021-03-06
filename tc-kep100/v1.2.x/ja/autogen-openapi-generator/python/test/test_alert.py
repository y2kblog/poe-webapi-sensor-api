"""
    PoE対応 WebAPI K型熱電対アンプ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 1.2.x
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import tc_kep100_client
from tc_kep100_client.model.alert_condition import AlertCondition
from tc_kep100_client.model.alert_ftp import AlertFtp
from tc_kep100_client.model.alert_target import AlertTarget
globals()['AlertCondition'] = AlertCondition
globals()['AlertFtp'] = AlertFtp
globals()['AlertTarget'] = AlertTarget
from tc_kep100_client.model.alert import Alert


class TestAlert(unittest.TestCase):
    """Alert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAlert(self):
        """Test Alert"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Alert()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

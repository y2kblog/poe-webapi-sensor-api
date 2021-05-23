# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.alert_condition import AlertCondition
from openapi_server.models.alert_target import AlertTarget
from openapi_server import util

from openapi_server.models.alert_condition import AlertCondition  # noqa: E501
from openapi_server.models.alert_target import AlertTarget  # noqa: E501

class AlertWithoutFTP(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, alert_id=None, mode=None, dst_ip=None, dst_port=80, path='/notify', timing='bothTriggerReset', period_sec=10, target=None, condition=None):  # noqa: E501
        """AlertWithoutFTP - a model defined in OpenAPI

        :param alert_id: The alert_id of this AlertWithoutFTP.  # noqa: E501
        :type alert_id: int
        :param mode: The mode of this AlertWithoutFTP.  # noqa: E501
        :type mode: str
        :param dst_ip: The dst_ip of this AlertWithoutFTP.  # noqa: E501
        :type dst_ip: List[int]
        :param dst_port: The dst_port of this AlertWithoutFTP.  # noqa: E501
        :type dst_port: int
        :param path: The path of this AlertWithoutFTP.  # noqa: E501
        :type path: str
        :param timing: The timing of this AlertWithoutFTP.  # noqa: E501
        :type timing: str
        :param period_sec: The period_sec of this AlertWithoutFTP.  # noqa: E501
        :type period_sec: int
        :param target: The target of this AlertWithoutFTP.  # noqa: E501
        :type target: AlertTarget
        :param condition: The condition of this AlertWithoutFTP.  # noqa: E501
        :type condition: AlertCondition
        """
        self.openapi_types = {
            'alert_id': int,
            'mode': str,
            'dst_ip': List[int],
            'dst_port': int,
            'path': str,
            'timing': str,
            'period_sec': int,
            'target': AlertTarget,
            'condition': AlertCondition
        }

        self.attribute_map = {
            'alert_id': 'alertId',
            'mode': 'mode',
            'dst_ip': 'dstIp',
            'dst_port': 'dstPort',
            'path': 'path',
            'timing': 'timing',
            'period_sec': 'periodSec',
            'target': 'target',
            'condition': 'condition'
        }

        self._alert_id = alert_id
        self._mode = mode
        self._dst_ip = dst_ip
        self._dst_port = dst_port
        self._path = path
        self._timing = timing
        self._period_sec = period_sec
        self._target = target
        self._condition = condition

    @classmethod
    def from_dict(cls, dikt) -> 'AlertWithoutFTP':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The alert_withoutFTP of this AlertWithoutFTP.  # noqa: E501
        :rtype: AlertWithoutFTP
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alert_id(self):
        """Gets the alert_id of this AlertWithoutFTP.

        アラートID   # noqa: E501

        :return: The alert_id of this AlertWithoutFTP.
        :rtype: int
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this AlertWithoutFTP.

        アラートID   # noqa: E501

        :param alert_id: The alert_id of this AlertWithoutFTP.
        :type alert_id: int
        """
        if alert_id is not None and alert_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `alert_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._alert_id = alert_id

    @property
    def mode(self):
        """Gets the mode of this AlertWithoutFTP.

        通知モード   省略時：webhook   'webhook'：Webhookモード。アラート情報をHTTPメッセージで通知する。   'ftp'：FTPモード。FTPサーバに対しアラート情報をCSVファイルで保存する。     # noqa: E501

        :return: The mode of this AlertWithoutFTP.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this AlertWithoutFTP.

        通知モード   省略時：webhook   'webhook'：Webhookモード。アラート情報をHTTPメッセージで通知する。   'ftp'：FTPモード。FTPサーバに対しアラート情報をCSVファイルで保存する。     # noqa: E501

        :param mode: The mode of this AlertWithoutFTP.
        :type mode: str
        """
        allowed_values = ["webhook", "ftp"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def dst_ip(self):
        """Gets the dst_ip of this AlertWithoutFTP.

        送信先IPアドレス（Webhookモード：通知先IPアドレス、FTPモード：FTPサーバのIPアドレス）   省略時：登録時のホストIP   USBからメッセージを受信した場合：通知先IPアドレス設定時はそのIPに対してアラートを送信する。省略時はUSBに対しアラートを送信する。   # noqa: E501

        :return: The dst_ip of this AlertWithoutFTP.
        :rtype: List[int]
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        """Sets the dst_ip of this AlertWithoutFTP.

        送信先IPアドレス（Webhookモード：通知先IPアドレス、FTPモード：FTPサーバのIPアドレス）   省略時：登録時のホストIP   USBからメッセージを受信した場合：通知先IPアドレス設定時はそのIPに対してアラートを送信する。省略時はUSBに対しアラートを送信する。   # noqa: E501

        :param dst_ip: The dst_ip of this AlertWithoutFTP.
        :type dst_ip: List[int]
        """
        if dst_ip is not None and len(dst_ip) > 4:
            raise ValueError("Invalid value for `dst_ip`, number of items must be less than or equal to `4`")  # noqa: E501
        if dst_ip is not None and len(dst_ip) < 4:
            raise ValueError("Invalid value for `dst_ip`, number of items must be greater than or equal to `4`")  # noqa: E501

        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        """Gets the dst_port of this AlertWithoutFTP.

        送信先ポート番号（Webhookモード：通知先ポート、FTPモード：FTPサーバの制御ポート）   省略時：80（Webhookモード）、21（FTPモード）   # noqa: E501

        :return: The dst_port of this AlertWithoutFTP.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """Sets the dst_port of this AlertWithoutFTP.

        送信先ポート番号（Webhookモード：通知先ポート、FTPモード：FTPサーバの制御ポート）   省略時：80（Webhookモード）、21（FTPモード）   # noqa: E501

        :param dst_port: The dst_port of this AlertWithoutFTP.
        :type dst_port: int
        """
        if dst_port is not None and dst_port < 0:  # noqa: E501
            raise ValueError("Invalid value for `dst_port`, must be a value greater than or equal to `0`")  # noqa: E501

        self._dst_port = dst_port

    @property
    def path(self):
        """Gets the path of this AlertWithoutFTP.

        送信先パス（Webhookモード：通知先エンドポイント、FTPモード：保存先パス）   省略時：'/notify'（Webhookモード）、'/'（FTPモード）   # noqa: E501

        :return: The path of this AlertWithoutFTP.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this AlertWithoutFTP.

        送信先パス（Webhookモード：通知先エンドポイント、FTPモード：保存先パス）   省略時：'/notify'（Webhookモード）、'/'（FTPモード）   # noqa: E501

        :param path: The path of this AlertWithoutFTP.
        :type path: str
        """
        if path is not None and len(path) > 32:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `32`")  # noqa: E501

        self._path = path

    @property
    def timing(self):
        """Gets the timing of this AlertWithoutFTP.

        通知/保存タイミングの設定   省略時：'bothTriggerReset'   'bothTriggerReset'：アラート発報時およびアラート復帰時（＝アラート状態変化時）に通知   'onlyTrigger'：アラート発報時のみ通知   'eachPeriod'：監視周期毎にアラート状態を継続して通知     # noqa: E501

        :return: The timing of this AlertWithoutFTP.
        :rtype: str
        """
        return self._timing

    @timing.setter
    def timing(self, timing):
        """Sets the timing of this AlertWithoutFTP.

        通知/保存タイミングの設定   省略時：'bothTriggerReset'   'bothTriggerReset'：アラート発報時およびアラート復帰時（＝アラート状態変化時）に通知   'onlyTrigger'：アラート発報時のみ通知   'eachPeriod'：監視周期毎にアラート状態を継続して通知     # noqa: E501

        :param timing: The timing of this AlertWithoutFTP.
        :type timing: str
        """
        allowed_values = ["bothTriggerReset", "onlyTrigger", "eachPeriod"]  # noqa: E501
        if timing not in allowed_values:
            raise ValueError(
                "Invalid value for `timing` ({0}), must be one of {1}"
                .format(timing, allowed_values)
            )

        self._timing = timing

    @property
    def period_sec(self):
        """Gets the period_sec of this AlertWithoutFTP.

        監視周期 [sec]   省略時：10   # noqa: E501

        :return: The period_sec of this AlertWithoutFTP.
        :rtype: int
        """
        return self._period_sec

    @period_sec.setter
    def period_sec(self, period_sec):
        """Sets the period_sec of this AlertWithoutFTP.

        監視周期 [sec]   省略時：10   # noqa: E501

        :param period_sec: The period_sec of this AlertWithoutFTP.
        :type period_sec: int
        """
        if period_sec is not None and period_sec < 1:  # noqa: E501
            raise ValueError("Invalid value for `period_sec`, must be a value greater than or equal to `1`")  # noqa: E501

        self._period_sec = period_sec

    @property
    def target(self):
        """Gets the target of this AlertWithoutFTP.


        :return: The target of this AlertWithoutFTP.
        :rtype: AlertTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this AlertWithoutFTP.


        :param target: The target of this AlertWithoutFTP.
        :type target: AlertTarget
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    @property
    def condition(self):
        """Gets the condition of this AlertWithoutFTP.


        :return: The condition of this AlertWithoutFTP.
        :rtype: AlertCondition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this AlertWithoutFTP.


        :param condition: The condition of this AlertWithoutFTP.
        :type condition: AlertCondition
        """
        if condition is None:
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501

        self._condition = condition
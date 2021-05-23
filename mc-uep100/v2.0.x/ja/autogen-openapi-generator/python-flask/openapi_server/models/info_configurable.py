# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InfoConfigurable(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, custom_name='"customName" is not set', blink_led=False):  # noqa: E501
        """InfoConfigurable - a model defined in OpenAPI

        :param custom_name: The custom_name of this InfoConfigurable.  # noqa: E501
        :type custom_name: str
        :param blink_led: The blink_led of this InfoConfigurable.  # noqa: E501
        :type blink_led: bool
        """
        self.openapi_types = {
            'custom_name': str,
            'blink_led': bool
        }

        self.attribute_map = {
            'custom_name': 'customName',
            'blink_led': 'blinkLed'
        }

        self._custom_name = custom_name
        self._blink_led = blink_led

    @classmethod
    def from_dict(cls, dikt) -> 'InfoConfigurable':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The info_configurable of this InfoConfigurable.  # noqa: E501
        :rtype: InfoConfigurable
        """
        return util.deserialize_model(dikt, cls)

    @property
    def custom_name(self):
        """Gets the custom_name of this InfoConfigurable.

        設定可能な名称   ユーザが識別を容易にするために利用する。   # noqa: E501

        :return: The custom_name of this InfoConfigurable.
        :rtype: str
        """
        return self._custom_name

    @custom_name.setter
    def custom_name(self, custom_name):
        """Sets the custom_name of this InfoConfigurable.

        設定可能な名称   ユーザが識別を容易にするために利用する。   # noqa: E501

        :param custom_name: The custom_name of this InfoConfigurable.
        :type custom_name: str
        """
        if custom_name is not None and len(custom_name) > 32:
            raise ValueError("Invalid value for `custom_name`, length must be less than or equal to `32`")  # noqa: E501

        self._custom_name = custom_name

    @property
    def blink_led(self):
        """Gets the blink_led of this InfoConfigurable.

        Status LED点滅の有無   `false`: デフォルト設定。Status LEDはネットワーク状態に対応した動作を行う   `true`: Status LEDを点滅させる（点灯時間と消灯時間は同一）   本設定は複数のPoE対応WebAPIセンサが設置され製品裏面に記載されたシリアルナンバーを確認できない場合に、どの機器が操作対象であるのかを目視で確認する際に利用する。   ※本設定は電源を再起動するとリセットされる。   # noqa: E501

        :return: The blink_led of this InfoConfigurable.
        :rtype: bool
        """
        return self._blink_led

    @blink_led.setter
    def blink_led(self, blink_led):
        """Sets the blink_led of this InfoConfigurable.

        Status LED点滅の有無   `false`: デフォルト設定。Status LEDはネットワーク状態に対応した動作を行う   `true`: Status LEDを点滅させる（点灯時間と消灯時間は同一）   本設定は複数のPoE対応WebAPIセンサが設置され製品裏面に記載されたシリアルナンバーを確認できない場合に、どの機器が操作対象であるのかを目視で確認する際に利用する。   ※本設定は電源を再起動するとリセットされる。   # noqa: E501

        :param blink_led: The blink_led of this InfoConfigurable.
        :type blink_led: bool
        """

        self._blink_led = blink_led

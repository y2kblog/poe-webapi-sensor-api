# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AlertTargetSetting(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, unit='Celsius'):  # noqa: E501
        """AlertTargetSetting - a model defined in OpenAPI

        :param unit: The unit of this AlertTargetSetting.  # noqa: E501
        :type unit: str
        """
        self.openapi_types = {
            'unit': str
        }

        self.attribute_map = {
            'unit': 'unit'
        }

        self._unit = unit

    @classmethod
    def from_dict(cls, dikt) -> 'AlertTargetSetting':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The alert_target_setting of this AlertTargetSetting.  # noqa: E501
        :rtype: AlertTargetSetting
        """
        return util.deserialize_model(dikt, cls)

    @property
    def unit(self):
        """Gets the unit of this AlertTargetSetting.

        単位(ケルビン、摂氏、華氏)   省略時：Celsius   # noqa: E501

        :return: The unit of this AlertTargetSetting.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AlertTargetSetting.

        単位(ケルビン、摂氏、華氏)   省略時：Celsius   # noqa: E501

        :param unit: The unit of this AlertTargetSetting.
        :type unit: str
        """
        allowed_values = ["Kelvin", "Celsius", "Fahrenheit"]  # noqa: E501
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"
                .format(unit, allowed_values)
            )

        self._unit = unit

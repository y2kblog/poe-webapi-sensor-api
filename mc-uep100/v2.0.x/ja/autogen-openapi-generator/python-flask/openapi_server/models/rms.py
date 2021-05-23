# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Rms(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lower_frq_hz=10, upper_frq_hz=80000, time_sec=0.0512):  # noqa: E501
        """Rms - a model defined in OpenAPI

        :param lower_frq_hz: The lower_frq_hz of this Rms.  # noqa: E501
        :type lower_frq_hz: int
        :param upper_frq_hz: The upper_frq_hz of this Rms.  # noqa: E501
        :type upper_frq_hz: int
        :param time_sec: The time_sec of this Rms.  # noqa: E501
        :type time_sec: float
        """
        self.openapi_types = {
            'lower_frq_hz': int,
            'upper_frq_hz': int,
            'time_sec': float
        }

        self.attribute_map = {
            'lower_frq_hz': 'lowerFrqHz',
            'upper_frq_hz': 'upperFrqHz',
            'time_sec': 'timeSec'
        }

        self._lower_frq_hz = lower_frq_hz
        self._upper_frq_hz = upper_frq_hz
        self._time_sec = time_sec

    @classmethod
    def from_dict(cls, dikt) -> 'Rms':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The rms of this Rms.  # noqa: E501
        :rtype: Rms
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lower_frq_hz(self):
        """Gets the lower_frq_hz of this Rms.

        取得する周波数帯域の下限値 (単位：Hz)    <!--省略時：10Hz  -->   # noqa: E501

        :return: The lower_frq_hz of this Rms.
        :rtype: int
        """
        return self._lower_frq_hz

    @lower_frq_hz.setter
    def lower_frq_hz(self, lower_frq_hz):
        """Sets the lower_frq_hz of this Rms.

        取得する周波数帯域の下限値 (単位：Hz)    <!--省略時：10Hz  -->   # noqa: E501

        :param lower_frq_hz: The lower_frq_hz of this Rms.
        :type lower_frq_hz: int
        """
        if lower_frq_hz is not None and lower_frq_hz >= 80000:  # noqa: E501
            raise ValueError("Invalid value for `lower_frq_hz`, must be a value less than `80000`")  # noqa: E501
        if lower_frq_hz is not None and lower_frq_hz < 10:  # noqa: E501
            raise ValueError("Invalid value for `lower_frq_hz`, must be a value greater than or equal to `10`")  # noqa: E501

        self._lower_frq_hz = lower_frq_hz

    @property
    def upper_frq_hz(self):
        """Gets the upper_frq_hz of this Rms.

        取得する周波数帯域の上限値 (単位：Hz)    <!--省略時：80kHz  -->   # noqa: E501

        :return: The upper_frq_hz of this Rms.
        :rtype: int
        """
        return self._upper_frq_hz

    @upper_frq_hz.setter
    def upper_frq_hz(self, upper_frq_hz):
        """Sets the upper_frq_hz of this Rms.

        取得する周波数帯域の上限値 (単位：Hz)    <!--省略時：80kHz  -->   # noqa: E501

        :param upper_frq_hz: The upper_frq_hz of this Rms.
        :type upper_frq_hz: int
        """
        if upper_frq_hz is not None and upper_frq_hz > 80000:  # noqa: E501
            raise ValueError("Invalid value for `upper_frq_hz`, must be a value less than or equal to `80000`")  # noqa: E501
        if upper_frq_hz is not None and upper_frq_hz <= 10:  # noqa: E501
            raise ValueError("Invalid value for `upper_frq_hz`, must be a value greater than `10`")  # noqa: E501

        self._upper_frq_hz = upper_frq_hz

    @property
    def time_sec(self):
        """Gets the time_sec of this Rms.

        測定時間 (単位：sec)     # noqa: E501

        :return: The time_sec of this Rms.
        :rtype: float
        """
        return self._time_sec

    @time_sec.setter
    def time_sec(self, time_sec):
        """Sets the time_sec of this Rms.

        測定時間 (単位：sec)     # noqa: E501

        :param time_sec: The time_sec of this Rms.
        :type time_sec: float
        """
        if time_sec is not None and time_sec <= 0:  # noqa: E501
            raise ValueError("Invalid value for `time_sec`, must be a value greater than `0`")  # noqa: E501

        self._time_sec = time_sec
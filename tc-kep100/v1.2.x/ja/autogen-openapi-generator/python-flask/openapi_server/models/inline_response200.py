# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.alert import Alert
from openapi_server import util

from openapi_server.models.alert import Alert  # noqa: E501

class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, alerts=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param alerts: The alerts of this InlineResponse200.  # noqa: E501
        :type alerts: List[Alert]
        """
        self.openapi_types = {
            'alerts': List[Alert]
        }

        self.attribute_map = {
            'alerts': 'alerts'
        }

        self._alerts = alerts

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alerts(self):
        """Gets the alerts of this InlineResponse200.


        :return: The alerts of this InlineResponse200.
        :rtype: List[Alert]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this InlineResponse200.


        :param alerts: The alerts of this InlineResponse200.
        :type alerts: List[Alert]
        """

        self._alerts = alerts
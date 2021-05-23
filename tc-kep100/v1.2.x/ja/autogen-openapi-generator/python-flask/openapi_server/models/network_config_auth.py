# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NetworkConfigAuth(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enable=False, method='Basic', user_name=None, password=None):  # noqa: E501
        """NetworkConfigAuth - a model defined in OpenAPI

        :param enable: The enable of this NetworkConfigAuth.  # noqa: E501
        :type enable: bool
        :param method: The method of this NetworkConfigAuth.  # noqa: E501
        :type method: str
        :param user_name: The user_name of this NetworkConfigAuth.  # noqa: E501
        :type user_name: str
        :param password: The password of this NetworkConfigAuth.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'enable': bool,
            'method': str,
            'user_name': str,
            'password': str
        }

        self.attribute_map = {
            'enable': 'enable',
            'method': 'method',
            'user_name': 'userName',
            'password': 'password'
        }

        self._enable = enable
        self._method = method
        self._user_name = user_name
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'NetworkConfigAuth':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The networkConfig_auth of this NetworkConfigAuth.  # noqa: E501
        :rtype: NetworkConfigAuth
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enable(self):
        """Gets the enable of this NetworkConfigAuth.

        認証機能の有効/無効   # noqa: E501

        :return: The enable of this NetworkConfigAuth.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this NetworkConfigAuth.

        認証機能の有効/無効   # noqa: E501

        :param enable: The enable of this NetworkConfigAuth.
        :type enable: bool
        """

        self._enable = enable

    @property
    def method(self):
        """Gets the method of this NetworkConfigAuth.

        認証方式   ※現バージョンではBasic認証のみサポート - \"Basic\"：Basic認証   # noqa: E501

        :return: The method of this NetworkConfigAuth.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this NetworkConfigAuth.

        認証方式   ※現バージョンではBasic認証のみサポート - \"Basic\"：Basic認証   # noqa: E501

        :param method: The method of this NetworkConfigAuth.
        :type method: str
        """
        allowed_values = ["Basic"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def user_name(self):
        """Gets the user_name of this NetworkConfigAuth.

        ユーザ名(最大20文字)   # noqa: E501

        :return: The user_name of this NetworkConfigAuth.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this NetworkConfigAuth.

        ユーザ名(最大20文字)   # noqa: E501

        :param user_name: The user_name of this NetworkConfigAuth.
        :type user_name: str
        """
        if user_name is not None and len(user_name) > 20:
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `20`")  # noqa: E501

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this NetworkConfigAuth.

        パスワード(最大20文字)   # noqa: E501

        :return: The password of this NetworkConfigAuth.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NetworkConfigAuth.

        パスワード(最大20文字)   # noqa: E501

        :param password: The password of this NetworkConfigAuth.
        :type password: str
        """
        if password is not None and len(password) > 20:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `20`")  # noqa: E501

        self._password = password

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AlertFtp(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, active_mode=False, add_sub_dir=False, user_name=None, password=None):  # noqa: E501
        """AlertFtp - a model defined in OpenAPI

        :param active_mode: The active_mode of this AlertFtp.  # noqa: E501
        :type active_mode: bool
        :param add_sub_dir: The add_sub_dir of this AlertFtp.  # noqa: E501
        :type add_sub_dir: bool
        :param user_name: The user_name of this AlertFtp.  # noqa: E501
        :type user_name: str
        :param password: The password of this AlertFtp.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'active_mode': bool,
            'add_sub_dir': bool,
            'user_name': str,
            'password': str
        }

        self.attribute_map = {
            'active_mode': 'activeMode',
            'add_sub_dir': 'addSubDir',
            'user_name': 'userName',
            'password': 'password'
        }

        self._active_mode = active_mode
        self._add_sub_dir = add_sub_dir
        self._user_name = user_name
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'AlertFtp':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The alert_ftp of this AlertFtp.  # noqa: E501
        :rtype: AlertFtp
        """
        return util.deserialize_model(dikt, cls)

    @property
    def active_mode(self):
        """Gets the active_mode of this AlertFtp.

        FTPアクティブモード/パッシブモードの選択   true：アクティブモード   false：パッシブモード   省略時：false（パッシブモード）   # noqa: E501

        :return: The active_mode of this AlertFtp.
        :rtype: bool
        """
        return self._active_mode

    @active_mode.setter
    def active_mode(self, active_mode):
        """Sets the active_mode of this AlertFtp.

        FTPアクティブモード/パッシブモードの選択   true：アクティブモード   false：パッシブモード   省略時：false（パッシブモード）   # noqa: E501

        :param active_mode: The active_mode of this AlertFtp.
        :type active_mode: bool
        """

        self._active_mode = active_mode

    @property
    def add_sub_dir(self):
        """Gets the add_sub_dir of this AlertFtp.

        保存先パスにサブフォルダを作成するかどうかの選択   true：サブフォルダを作成する   false：サブフォルダを作成しない   省略時：false   サブフォルダは'path'で指定されたディレクトリの下に作成される。   <br>**サブフォルダ名の規則**   `{serialNumber}_xxx`   xxxxは0埋め3桁の数値（初期値は001）。製品が再起動されるごとに新たなフォルダが連番で作成される。   例：'addSubDir'がtrue、'path'が`/dir1/dir2`、'serialNumber'が`abcdefghij`のとき、`/dir1/dir2/abcdefghij_001/`以下に通知ファイルが保存される   # noqa: E501

        :return: The add_sub_dir of this AlertFtp.
        :rtype: bool
        """
        return self._add_sub_dir

    @add_sub_dir.setter
    def add_sub_dir(self, add_sub_dir):
        """Sets the add_sub_dir of this AlertFtp.

        保存先パスにサブフォルダを作成するかどうかの選択   true：サブフォルダを作成する   false：サブフォルダを作成しない   省略時：false   サブフォルダは'path'で指定されたディレクトリの下に作成される。   <br>**サブフォルダ名の規則**   `{serialNumber}_xxx`   xxxxは0埋め3桁の数値（初期値は001）。製品が再起動されるごとに新たなフォルダが連番で作成される。   例：'addSubDir'がtrue、'path'が`/dir1/dir2`、'serialNumber'が`abcdefghij`のとき、`/dir1/dir2/abcdefghij_001/`以下に通知ファイルが保存される   # noqa: E501

        :param add_sub_dir: The add_sub_dir of this AlertFtp.
        :type add_sub_dir: bool
        """

        self._add_sub_dir = add_sub_dir

    @property
    def user_name(self):
        """Gets the user_name of this AlertFtp.

        FTPサーバのユーザ名(最大20文字)   ※FTPモード時のみ有効   # noqa: E501

        :return: The user_name of this AlertFtp.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AlertFtp.

        FTPサーバのユーザ名(最大20文字)   ※FTPモード時のみ有効   # noqa: E501

        :param user_name: The user_name of this AlertFtp.
        :type user_name: str
        """
        if user_name is not None and len(user_name) > 20:
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `20`")  # noqa: E501

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this AlertFtp.

        FTPサーバのパスワード(最大20文字)   ※FTPモード時のみ有効   # noqa: E501

        :return: The password of this AlertFtp.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AlertFtp.

        FTPサーバのパスワード(最大20文字)   ※FTPモード時のみ有効   # noqa: E501

        :param password: The password of this AlertFtp.
        :type password: str
        """
        if password is not None and len(password) > 20:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `20`")  # noqa: E501

        self._password = password

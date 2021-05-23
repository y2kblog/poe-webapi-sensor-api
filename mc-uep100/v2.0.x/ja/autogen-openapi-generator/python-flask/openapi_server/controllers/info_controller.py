import connexion
import six

from openapi_server.models.info import Info  # noqa: E501
from openapi_server.models.info_configurable import InfoConfigurable  # noqa: E501
from openapi_server import util


def info_get():  # noqa: E501
    """機器情報の取得

    機器情報を取得する。   /info.html にブラウザからアクセスし取得することも可能  # noqa: E501


    :rtype: Info
    """
    return 'do some magic!'


def info_patch(info_configurable=None):  # noqa: E501
    """設定変更が可能な機器情報の変更

    指定したフィールドの値を変更する。   指定されなかったフィールドの値は変更されない。   /info.html にブラウザからアクセスし操作することも可能  # noqa: E501

    :param info_configurable: 省略したパラメータは変更されない
    :type info_configurable: dict | bytes

    :rtype: InfoConfigurable
    """
    if connexion.request.is_json:
        info_configurable = InfoConfigurable.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

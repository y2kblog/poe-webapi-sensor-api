import connexion
import six

from openapi_server.models.network_config import NetworkConfig  # noqa: E501
from openapi_server import util


def config_network_get():  # noqa: E501
    """ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得

    ネットワーク設定情報を取得する。   初期設定は認証機能：無効、DHCP：有効です。  # noqa: E501


    :rtype: NetworkConfig
    """
    return 'do some magic!'


def config_network_patch(network_config=None):  # noqa: E501
    """ネットワーク設定（認証機能・DHCP・手動IP）の変更

    指定したフィールドの値を変更する。 指定されなかったフィールドの値は変更されない。   変更に成功した場合、応答後にシステムは自動的に再起動する。   /config/network.html にブラウザからアクセスし操作することも可能  # noqa: E501

    :param network_config: 省略したパラメータは変更されない
    :type network_config: dict | bytes

    :rtype: NetworkConfig
    """
    if connexion.request.is_json:
        network_config = NetworkConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

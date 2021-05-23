import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.raw_setting import RawSetting  # noqa: E501
from openapi_server import util


def raw_delete():  # noqa: E501
    """生値取得終了

    時系列音圧データの取得を停止する。   /raw.html にブラウザからアクセスし操作することも可能  # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def raw_post(raw_setting=None):  # noqa: E501
    """生値取得開始

    時系列音圧データの取得を開始する。   /raw.html にブラウザからアクセスし操作することも可能   ※送信する音圧データの仕様は以下の\&quot;Callbacks\&quot;タブに記載  # noqa: E501

    :param raw_setting: 設定用パラメータを指定
    :type raw_setting: dict | bytes

    :rtype: RawSetting
    """
    if connexion.request.is_json:
        raw_setting = RawSetting.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def raw_status_get():  # noqa: E501
    """生値取得状態の取得

     # noqa: E501


    :rtype: RawSetting
    """
    return 'do some magic!'

import connexion
import six

from openapi_server.models.alert import Alert  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server import util


def add_alert_setting(alert=None):  # noqa: E501
    """アラート設定を1つ登録

    指定した条件を満たしたときにWebhookによる通知やFTPサーバにCSV形式で保存するアラート機能の設定を1つ登録する。   製品の電源を切ってもアラート設定は保持される。アラート設定の削除か製品の初期化を行うことで設定が消去される。   アラート設定は最大5個まで設定可能   /alerts.html にブラウザからアクセスし操作することも可能   ※通知データの仕様は以下の\&quot;Callbacks\&quot;タブに記載  # noqa: E501

    :param alert: 
    :type alert: dict | bytes

    :rtype: Alert
    """
    if connexion.request.is_json:
        alert = Alert.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def alerts_alert_id_delete(alert_id):  # noqa: E501
    """指定したidのアラート設定を削除

    指定したidのアラート設定を削除する。  # noqa: E501

    :param alert_id: 取得したいアラート設定のID
    :type alert_id: int

    :rtype: None
    """
    return 'do some magic!'


def alerts_delete():  # noqa: E501
    """登録済みアラート設定を全て削除

    登録済みアラート設定を全て削除する。   /alerts.html にブラウザからアクセスし操作することも可能  # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_alert_by_id(alert_id):  # noqa: E501
    """指定したidのアラート設定を取得

     # noqa: E501

    :param alert_id: 取得したいアラート設定のID
    :type alert_id: int

    :rtype: Alert
    """
    return 'do some magic!'


def get_alerts():  # noqa: E501
    """登録済みアラート設定一覧を取得

    登録済みのアラートの一覧を取得する。  # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'

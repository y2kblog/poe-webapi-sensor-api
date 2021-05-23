import connexion
import six

from openapi_server import util


def init_put():  # noqa: E501
    """製品を初期状態に戻す

    - 生値取得中の場合、生値取得を終了する - ネットワーク設定を初期状態へ戻す   その後、自動的に再起動する   /init.html にブラウザからアクセスし操作することも可能  # noqa: E501


    :rtype: None
    """
    return 'do some magic!'

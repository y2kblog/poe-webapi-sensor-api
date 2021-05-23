import connexion
import six

from openapi_server.models.temperature import Temperature  # noqa: E501
from openapi_server import util


def temperature_get(unit=None):  # noqa: E501
    """熱電対の温度の取得

    熱電対の温接点温度を取得する。   /temperature.html にブラウザからアクセスすることで周期的に温度を取得することも可能    # noqa: E501

    :param unit: 単位(ケルビン、摂氏、華氏)   省略時：Celsius 
    :type unit: str

    :rtype: Temperature
    """
    return 'do some magic!'

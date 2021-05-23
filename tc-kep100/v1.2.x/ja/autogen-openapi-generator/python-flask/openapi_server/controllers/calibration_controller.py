import connexion
import six

from openapi_server.models.thermocouple_calib import ThermocoupleCalib  # noqa: E501
from openapi_server import util


def calibration_get():  # noqa: E501
    """校正パラメータの取得

    熱電対の校正パラメータを取得する。   /calibration.html にブラウザからアクセスし取得することも可能  # noqa: E501


    :rtype: ThermocoupleCalib
    """
    return 'do some magic!'


def calibration_put(thermocouple_calib=None):  # noqa: E501
    """熱電対の校正を実行

    熱電対の校正パラメータを変更する。   /calibration.html にブラウザからアクセスし操作することも可能  # noqa: E501

    :param thermocouple_calib: 
    :type thermocouple_calib: dict | bytes

    :rtype: ThermocoupleCalib
    """
    if connexion.request.is_json:
        thermocouple_calib = ThermocoupleCalib.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

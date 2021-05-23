import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.rms_result import RmsResult  # noqa: E501
from openapi_server import util


def get_rms(lower_frq_hz=None, upper_frq_hz=None, time_sec=None):  # noqa: E501
    """音圧のRMS値を取得

    音圧の実効値を音圧レベル表示した値。   周波数帯域を指定することで、 指定した周波数帯域の音圧の部分オーバーオール値(POA：Partial OverAll)の測定も可能。  # noqa: E501

    :param lower_frq_hz: 取得する周波数帯域の下限値 (単位：Hz)    &lt;!--省略時：10Hz  --&gt; 
    :type lower_frq_hz: int
    :param upper_frq_hz: 取得する周波数帯域の上限値 (単位：Hz)    &lt;!--省略時：80kHz  --&gt; 
    :type upper_frq_hz: int
    :param time_sec: 測定時間 (単位：sec)   
    :type time_sec: float

    :rtype: RmsResult
    """
    return 'do some magic!'

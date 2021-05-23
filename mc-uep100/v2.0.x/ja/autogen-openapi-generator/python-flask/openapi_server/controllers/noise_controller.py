import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.sound_level_result import SoundLevelResult  # noqa: E501
from openapi_server import util


def get_noise(time_sec=None, time_weight=None):  # noqa: E501
    """騒音レベルの取得 

    下記3項目を測定する。 周波数重み付け特性はA特性を適用する。  - 等価騒音レベル(Leq)   Equivalent continuous A-weighted sound pressure level.   指定した測定時間内の騒音の総エネルギーの時間平均値を音圧レベル表示した値。   環境騒音の評価量として用いられる。    - 単発騒音暴露レベル(SEL)   Single Event Noise exposure level.   単発的に発生する騒音の全エネルギーと等しいエネルギーを持つ継続時間1秒間の定常音の音圧レベルに換算した値。   単発的または間欠的に発生する継続時間の短い騒音を測定する評価量として用いられる。    - ピーク音圧レベル(Lpeak)   指定した測定時間内の騒音の最大値を音圧レベル表示した値。    ※本製品はJIS C 1509や計量法に定められた騒音計には適合しておりません。  # noqa: E501

    :param time_sec: 測定時間 (単位：sec)    省略時：0.1024 sec 
    :type time_sec: float
    :param time_weight: 時間重み付け特性   省略時：Slow   - \&quot;slow\&quot;：時定数1sec。   - \&quot;fast\&quot;：時定数0.125sec。   - \&quot;impulse\&quot;：時定数0.035sec。 
    :type time_weight: str

    :rtype: SoundLevelResult
    """
    return 'do some magic!'

"""
    PoE対応 WebAPI 超音波センサ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 2.0.x
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from myapi.api_client import ApiClient, Endpoint as _Endpoint
from myapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from myapi.model.error import Error
from myapi.model.rms_result import RmsResult


class RmsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_rms(
            self,
            **kwargs
        ):
            """音圧のRMS値を取得  # noqa: E501

            音圧の実効値を音圧レベル表示した値。   周波数帯域を指定することで、 指定した周波数帯域の音圧の部分オーバーオール値(POA：Partial OverAll)の測定も可能。   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_rms(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                lower_frq_hz (int): 取得する周波数帯域の下限値 (単位：Hz)    <!--省略時：10Hz  --> . [optional] if omitted the server will use the default value of 10
                upper_frq_hz (int): 取得する周波数帯域の上限値 (単位：Hz)    <!--省略時：80kHz  --> . [optional] if omitted the server will use the default value of 80000
                time_sec (float): 測定時間 (単位：sec)   . [optional] if omitted the server will use the default value of 0.0256
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                RmsResult
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_rms = _Endpoint(
            settings={
                'response_type': (RmsResult,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/rms',
                'operation_id': 'get_rms',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lower_frq_hz',
                    'upper_frq_hz',
                    'time_sec',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'lower_frq_hz',
                    'upper_frq_hz',
                    'time_sec',
                ]
            },
            root_map={
                'validations': {
                    ('lower_frq_hz',): {

                        'exclusive_maximum': 80000,
                        'inclusive_minimum': 10,
                    },
                    ('upper_frq_hz',): {

                        'inclusive_maximum': 80000,
                        'exclusive_minimum': 10,
                    },
                    ('time_sec',): {

                        'exclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lower_frq_hz':
                        (int,),
                    'upper_frq_hz':
                        (int,),
                    'time_sec':
                        (float,),
                },
                'attribute_map': {
                    'lower_frq_hz': 'lowerFrqHz',
                    'upper_frq_hz': 'upperFrqHz',
                    'time_sec': 'timeSec',
                },
                'location_map': {
                    'lower_frq_hz': 'query',
                    'upper_frq_hz': 'query',
                    'time_sec': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_rms
        )

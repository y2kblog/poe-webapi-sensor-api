"""
    PoE対応 WebAPI K型熱電対アンプ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 1.2.x
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from tc_kep100_client.api_client import ApiClient, Endpoint as _Endpoint
from tc_kep100_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from tc_kep100_client.model.temperature import Temperature


class TemperatureApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __temperature_get(
            self,
            **kwargs
        ):
            """熱電対の温度の取得  # noqa: E501

            熱電対の温接点温度を取得する。   /temperature.html にブラウザからアクセスすることで周期的に温度を取得することも可能     # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.temperature_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                unit (str): 単位(ケルビン、摂氏、華氏)   省略時：Celsius . [optional]
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
                Temperature
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

        self.temperature_get = _Endpoint(
            settings={
                'response_type': (Temperature,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/temperature',
                'operation_id': 'temperature_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'unit',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'unit',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('unit',): {

                        "KELVIN": "Kelvin",
                        "CELSIUS": "Celsius",
                        "FAHRENHEIT": "Fahrenheit"
                    },
                },
                'openapi_types': {
                    'unit':
                        (str,),
                },
                'attribute_map': {
                    'unit': 'unit',
                },
                'location_map': {
                    'unit': 'query',
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
            callable=__temperature_get
        )

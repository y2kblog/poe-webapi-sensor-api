# openapi_client.NoiseApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_noise**](NoiseApi.md#get_noise) | **GET** /noise | 騒音レベルの取得 


# **get_noise**
> SoundLevelResult get_noise()

騒音レベルの取得 

下記3項目を測定する。 周波数重み付け特性はA特性を適用する。  - 等価騒音レベル(Leq)   Equivalent continuous A-weighted sound pressure level.   指定した測定時間内の騒音の総エネルギーの時間平均値を音圧レベル表示した値。   環境騒音の評価量として用いられる。    - 単発騒音暴露レベル(SEL)   Single Event Noise exposure level.   単発的に発生する騒音の全エネルギーと等しいエネルギーを持つ継続時間1秒間の定常音の音圧レベルに換算した値。   単発的または間欠的に発生する継続時間の短い騒音を測定する評価量として用いられる。    - ピーク音圧レベル(Lpeak)   指定した測定時間内の騒音の最大値を音圧レベル表示した値。    ※本製品はJIS C 1509や計量法に定められた騒音計には適合しておりません。 

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import noise_api
from openapi_client.model.sound_level_result import SoundLevelResult
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = noise_api.NoiseApi(api_client)
    time_sec = 0.5 # float | 測定時間 (単位：sec)    省略時：0.1024 sec  (optional)
    time_weight = "slow" # str | 時間重み付け特性   省略時：Slow   - \"slow\"：時定数1sec。   - \"fast\"：時定数0.125sec。   - \"impulse\"：時定数0.035sec。  (optional) if omitted the server will use the default value of "slow"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 騒音レベルの取得 
        api_response = api_instance.get_noise(time_sec=time_sec, time_weight=time_weight)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NoiseApi->get_noise: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_sec** | **float**| 測定時間 (単位：sec)    省略時：0.1024 sec  | [optional]
 **time_weight** | **str**| 時間重み付け特性   省略時：Slow   - \&quot;slow\&quot;：時定数1sec。   - \&quot;fast\&quot;：時定数0.125sec。   - \&quot;impulse\&quot;：時定数0.035sec。  | [optional] if omitted the server will use the default value of "slow"

### Return type

[**SoundLevelResult**](SoundLevelResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 測定成功 |  -  |
**409** | 生値を取得中のため測定できない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


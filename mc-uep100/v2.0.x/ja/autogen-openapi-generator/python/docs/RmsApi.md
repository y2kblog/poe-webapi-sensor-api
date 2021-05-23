# openapi_client.RmsApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rms**](RmsApi.md#get_rms) | **GET** /rms | 音圧のRMS値を取得


# **get_rms**
> RmsResult get_rms()

音圧のRMS値を取得

音圧の実効値を音圧レベル表示した値。   周波数帯域を指定することで、 指定した周波数帯域の音圧の部分オーバーオール値(POA：Partial OverAll)の測定も可能。 

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import rms_api
from openapi_client.model.rms_result import RmsResult
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
    api_instance = rms_api.RmsApi(api_client)
    lower_frq_hz = 1000 # int | 取得する周波数帯域の下限値 (単位：Hz)    <!--省略時：10Hz  -->  (optional) if omitted the server will use the default value of 10
    upper_frq_hz = 10000 # int | 取得する周波数帯域の上限値 (単位：Hz)    <!--省略時：80kHz  -->  (optional) if omitted the server will use the default value of 80000
    time_sec = 0.5 # float | 測定時間 (単位：sec)    (optional) if omitted the server will use the default value of 0.0256

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 音圧のRMS値を取得
        api_response = api_instance.get_rms(lower_frq_hz=lower_frq_hz, upper_frq_hz=upper_frq_hz, time_sec=time_sec)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RmsApi->get_rms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_frq_hz** | **int**| 取得する周波数帯域の下限値 (単位：Hz)    &lt;!--省略時：10Hz  --&gt;  | [optional] if omitted the server will use the default value of 10
 **upper_frq_hz** | **int**| 取得する周波数帯域の上限値 (単位：Hz)    &lt;!--省略時：80kHz  --&gt;  | [optional] if omitted the server will use the default value of 80000
 **time_sec** | **float**| 測定時間 (単位：sec)    | [optional] if omitted the server will use the default value of 0.0256

### Return type

[**RmsResult**](RmsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 測定成功 |  -  |
**429** | 生値取得中のため取得不可能 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


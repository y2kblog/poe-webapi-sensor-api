# mc_uep100_client.RawApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**raw_delete**](RawApi.md#raw_delete) | **DELETE** /raw | 生値取得終了
[**raw_post**](RawApi.md#raw_post) | **POST** /raw | 生値取得開始
[**raw_status_get**](RawApi.md#raw_status_get) | **GET** /raw-status | 生値取得状態の取得


# **raw_delete**
> raw_delete()

生値取得終了

時系列音圧データの取得を停止する。   /raw.html にブラウザからアクセスし操作することも可能 

### Example

* Basic Authentication (basicAuth):
```python
import time
import mc_uep100_client
from mc_uep100_client.api import raw_api
from pprint import pprint
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = mc_uep100_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mc_uep100_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mc_uep100_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = raw_api.RawApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 生値取得終了
        api_instance.raw_delete()
    except mc_uep100_client.ApiException as e:
        print("Exception when calling RawApi->raw_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 生値の取得終了に成功   この応答の前に、キー\&quot;final\&quot;をtrueとしたUDPパケットを送信する。  |  -  |
**409** | 生値の取得が開始されていない  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **raw_post**
> RawSetting raw_post()

生値取得開始

時系列音圧データの取得を開始する。   /raw.html にブラウザからアクセスし操作することも可能   ※送信する音圧データの仕様は以下の\"Callbacks\"タブに記載 

### Example

* Basic Authentication (basicAuth):
```python
import time
import mc_uep100_client
from mc_uep100_client.api import raw_api
from mc_uep100_client.model.error import Error
from mc_uep100_client.model.raw_setting import RawSetting
from pprint import pprint
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = mc_uep100_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mc_uep100_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mc_uep100_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = raw_api.RawApi(api_client)
    raw_setting = RawSetting(
        dst_ip=[192, 168, 1, 2],
        dst_port=10000,
        frq_hz=160000,
        data_num=8192,
    ) # RawSetting | 設定用パラメータを指定 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 生値取得開始
        api_response = api_instance.raw_post(raw_setting=raw_setting)
        pprint(api_response)
    except mc_uep100_client.ApiException as e:
        print("Exception when calling RawApi->raw_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_setting** | [**RawSetting**](RawSetting.md)| 設定用パラメータを指定 | [optional]

### Return type

[**RawSetting**](RawSetting.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | リクエストを受け付けた。生値送信開始 |  -  |
**409** | 既に生値取得処理を行っているため取得開始できない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **raw_status_get**
> RawSetting raw_status_get()

生値取得状態の取得

### Example

* Basic Authentication (basicAuth):
```python
import time
import mc_uep100_client
from mc_uep100_client.api import raw_api
from mc_uep100_client.model.raw_setting import RawSetting
from pprint import pprint
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = mc_uep100_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mc_uep100_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mc_uep100_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = raw_api.RawApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 生値取得状態の取得
        api_response = api_instance.raw_status_get()
        pprint(api_response)
    except mc_uep100_client.ApiException as e:
        print("Exception when calling RawApi->raw_status_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RawSetting**](RawSetting.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 生値取得状態を応答  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


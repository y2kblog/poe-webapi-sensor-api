# tc_kep100_client.InfoApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_get**](InfoApi.md#info_get) | **GET** /info | 機器情報の取得
[**info_patch**](InfoApi.md#info_patch) | **PATCH** /info | 設定変更が可能な機器情報の変更


# **info_get**
> Info info_get()

機器情報の取得

機器情報を取得する。   /info.html にブラウザからアクセスし取得することも可能 

### Example

* Basic Authentication (basicAuth):
```python
import time
import tc_kep100_client
from tc_kep100_client.api import info_api
from tc_kep100_client.model.info import Info
from pprint import pprint
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = tc_kep100_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = tc_kep100_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with tc_kep100_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = info_api.InfoApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 機器情報の取得
        api_response = api_instance.info_get()
        pprint(api_response)
    except tc_kep100_client.ApiException as e:
        print("Exception when calling InfoApi->info_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Info**](Info.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 機器情報を応答 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_patch**
> InfoConfigurable info_patch()

設定変更が可能な機器情報の変更

指定したフィールドの値を変更する。   指定されなかったフィールドの値は変更されない。   /info.html にブラウザからアクセスし操作することも可能 

### Example

* Basic Authentication (basicAuth):
```python
import time
import tc_kep100_client
from tc_kep100_client.api import info_api
from tc_kep100_client.model.info_configurable import InfoConfigurable
from pprint import pprint
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = tc_kep100_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = tc_kep100_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with tc_kep100_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = info_api.InfoApi(api_client)
    info_configurable = InfoConfigurable(
        custom_name="sensor_1",
        blink_led=False,
    ) # InfoConfigurable | 省略したパラメータは変更されない (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 設定変更が可能な機器情報の変更
        api_response = api_instance.info_patch(info_configurable=info_configurable)
        pprint(api_response)
    except tc_kep100_client.ApiException as e:
        print("Exception when calling InfoApi->info_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info_configurable** | [**InfoConfigurable**](InfoConfigurable.md)| 省略したパラメータは変更されない | [optional]

### Return type

[**InfoConfigurable**](InfoConfigurable.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 指定した機器情報の変更に成功   ※省略したパラメータは表示されない  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ct_ep100_client.Co2Api

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**co2_get**](Co2Api.md#co2_get) | **GET** /co2 | 二酸化炭素濃度の取得
[**config_co2_get**](Co2Api.md#config_co2_get) | **GET** /config/co2 | 二酸化炭素センサの設定の取得
[**config_co2_patch**](Co2Api.md#config_co2_patch) | **PATCH** /config/co2 | 二酸化炭素センサの設定の変更


# **co2_get**
> Co2 co2_get()

二酸化炭素濃度の取得

二酸化炭素濃度を取得する。   /co2.html にブラウザからアクセスすることで周期的に温度を取得することも可能   

### Example

* Basic Authentication (basicAuth):
```python
import time
import ct_ep100_client
from ct_ep100_client.api import co2_api
from ct_ep100_client.model.co2 import Co2
from pprint import pprint
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = ct_ep100_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ct_ep100_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ct_ep100_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = co2_api.Co2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 二酸化炭素濃度の取得
        api_response = api_instance.co2_get()
        pprint(api_response)
    except ct_ep100_client.ApiException as e:
        print("Exception when calling Co2Api->co2_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Co2**](Co2.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | センサ情報を応答 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_co2_get**
> ConfigCo2 config_co2_get()

二酸化炭素センサの設定の取得

### Example

* Basic Authentication (basicAuth):
```python
import time
import ct_ep100_client
from ct_ep100_client.api import co2_api
from ct_ep100_client.model.config_co2 import ConfigCo2
from pprint import pprint
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = ct_ep100_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ct_ep100_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ct_ep100_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = co2_api.Co2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 二酸化炭素センサの設定の取得
        api_response = api_instance.config_co2_get()
        pprint(api_response)
    except ct_ep100_client.ApiException as e:
        print("Exception when calling Co2Api->config_co2_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigCo2**](ConfigCo2.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 二酸化炭素センサの設定の取得に成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_co2_patch**
> ConfigCo2 config_co2_patch()

二酸化炭素センサの設定の変更

指定したフィールドの値を変更する。 指定されなかったフィールドの値は変更されない。   /config/co2.html にブラウザからアクセスすることでも設定変更が可能   

### Example

* Basic Authentication (basicAuth):
```python
import time
import ct_ep100_client
from ct_ep100_client.api import co2_api
from ct_ep100_client.model.config_co2 import ConfigCo2
from pprint import pprint
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = ct_ep100_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ct_ep100_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ct_ep100_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = co2_api.Co2Api(api_client)
    config_co2 = ConfigCo2(
        enable_asc=False,
    ) # ConfigCo2 | 省略したパラメータはデフォルト値が適用される (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 二酸化炭素センサの設定の変更
        api_response = api_instance.config_co2_patch(config_co2=config_co2)
        pprint(api_response)
    except ct_ep100_client.ApiException as e:
        print("Exception when calling Co2Api->config_co2_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_co2** | [**ConfigCo2**](ConfigCo2.md)| 省略したパラメータはデフォルト値が適用される | [optional]

### Return type

[**ConfigCo2**](ConfigCo2.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 二酸化炭素センサの設定の変更に成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


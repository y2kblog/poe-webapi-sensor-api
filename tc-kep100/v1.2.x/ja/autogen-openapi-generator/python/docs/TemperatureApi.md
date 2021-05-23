# openapi_client.TemperatureApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temperature_get**](TemperatureApi.md#temperature_get) | **GET** /temperature | 熱電対の温度の取得


# **temperature_get**
> Temperature temperature_get()

熱電対の温度の取得

熱電対の温接点温度を取得する。   /temperature.html にブラウザからアクセスすることで周期的に温度を取得することも可能   

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import temperature_api
from openapi_client.model.temperature import Temperature
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
    api_instance = temperature_api.TemperatureApi(api_client)
    unit = "Kelvin" # str | 単位(ケルビン、摂氏、華氏)   省略時：Celsius  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 熱電対の温度の取得
        api_response = api_instance.temperature_get(unit=unit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemperatureApi->temperature_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit** | **str**| 単位(ケルビン、摂氏、華氏)   省略時：Celsius  | [optional]

### Return type

[**Temperature**](Temperature.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 温度情報を応答 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


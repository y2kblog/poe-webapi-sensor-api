# openapi_client.InitApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**init_put**](InitApi.md#init_put) | **PUT** /init | 製品を初期状態に戻す


# **init_put**
> init_put()

製品を初期状態に戻す

- 生値取得中の場合、生値取得を終了する - ネットワーク設定を初期状態へ戻す   その後、自動的に再起動する   /init.html にブラウザからアクセスし操作することも可能 

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import init_api
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
    api_instance = init_api.InitApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 製品を初期状態に戻す
        api_instance.init_put()
    except openapi_client.ApiException as e:
        print("Exception when calling InitApi->init_put: %s\n" % e)
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
**200** | 初期化に成功   このレスポンスの後、自動的に再起動する  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


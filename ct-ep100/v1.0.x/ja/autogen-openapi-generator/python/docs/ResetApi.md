# ct_ep100_client.ResetApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_put**](ResetApi.md#reset_put) | **PUT** /reset | 製品を再起動する


# **reset_put**
> reset_put()

製品を再起動する

製品を再起動する。   /reset.html にブラウザからアクセスし操作することも可能 

### Example

* Basic Authentication (basicAuth):
```python
import time
import ct_ep100_client
from ct_ep100_client.api import reset_api
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
    api_instance = reset_api.ResetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 製品を再起動する
        api_instance.reset_put()
    except ct_ep100_client.ApiException as e:
        print("Exception when calling ResetApi->reset_put: %s\n" % e)
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
**200** | このレスポンスの後、自動的に再起動する  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


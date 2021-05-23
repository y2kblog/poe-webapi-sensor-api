# mc_uep100_client.NetworkApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_network_get**](NetworkApi.md#config_network_get) | **GET** /config/network | ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得
[**config_network_patch**](NetworkApi.md#config_network_patch) | **PATCH** /config/network | ネットワーク設定（認証機能・DHCP・手動IP）の変更


# **config_network_get**
> NetworkConfig config_network_get()

ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得

ネットワーク設定情報を取得する。   初期設定は認証機能：無効、DHCP：有効です。 

### Example

* Basic Authentication (basicAuth):
```python
import time
import mc_uep100_client
from mc_uep100_client.api import network_api
from mc_uep100_client.model.network_config import NetworkConfig
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
    api_instance = network_api.NetworkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得
        api_response = api_instance.config_network_get()
        pprint(api_response)
    except mc_uep100_client.ApiException as e:
        print("Exception when calling NetworkApi->config_network_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkConfig**](NetworkConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ネットワーク設定の取得に成功  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_network_patch**
> NetworkConfig config_network_patch()

ネットワーク設定（認証機能・DHCP・手動IP）の変更

指定したフィールドの値を変更する。 指定されなかったフィールドの値は変更されない。   変更に成功した場合、応答後にシステムは自動的に再起動する。   /config/network.html にブラウザからアクセスし操作することも可能 

### Example

* Basic Authentication (basicAuth):
```python
import time
import mc_uep100_client
from mc_uep100_client.api import network_api
from mc_uep100_client.model.network_config import NetworkConfig
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
    api_instance = network_api.NetworkApi(api_client)
    network_config = NetworkConfig(
        auth=NetworkConfigAuth(
            enable=False,
            method="Basic",
            user_name="user",
            password="password",
        ),
        dhcp=NetworkConfigDhcp(
            enable=True,
        ),
        enable_mdns=True,
        static_ip_address=[192, 168, 1, 100],
        static_subnet_mask=[255, 255, 255, 0],
        static_default_gateway=[192, 168, 1, 1],
        static_dns_server=[192, 168, 1, 1],
    ) # NetworkConfig | 省略したパラメータは変更されない (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ネットワーク設定（認証機能・DHCP・手動IP）の変更
        api_response = api_instance.config_network_patch(network_config=network_config)
        pprint(api_response)
    except mc_uep100_client.ApiException as e:
        print("Exception when calling NetworkApi->config_network_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_config** | [**NetworkConfig**](NetworkConfig.md)| 省略したパラメータは変更されない | [optional]

### Return type

[**NetworkConfig**](NetworkConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ネットワーク設定の変更に成功   ※省略したパラメータは表示されない  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


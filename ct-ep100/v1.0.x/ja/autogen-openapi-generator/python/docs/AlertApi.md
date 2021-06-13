# ct_ep100_client.AlertApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_alert_setting**](AlertApi.md#add_alert_setting) | **POST** /alerts | アラート設定を1つ登録
[**alerts_alert_id_delete**](AlertApi.md#alerts_alert_id_delete) | **DELETE** /alerts/{alertId} | 指定したidのアラート設定を削除
[**alerts_delete**](AlertApi.md#alerts_delete) | **DELETE** /alerts | 登録済みアラート設定を全て削除
[**get_alert_by_id**](AlertApi.md#get_alert_by_id) | **GET** /alerts/{alertId} | 指定したidのアラート設定を取得
[**get_alerts**](AlertApi.md#get_alerts) | **GET** /alerts | 登録済みアラート設定一覧を取得


# **add_alert_setting**
> Alert add_alert_setting()

アラート設定を1つ登録

指定した条件を満たしたときにWebhookによる通知やFTPサーバにCSV形式で保存するアラート機能の設定を1つ登録する。   製品の電源を切ってもアラート設定は保持される。アラート設定の削除か製品の初期化を行うことで設定が消去される。   アラート設定は最大5個まで設定可能   /alerts.html にブラウザからアクセスし操作することも可能   ※通知データの仕様は以下の\"Callbacks\"タブに記載 

### Example

* Basic Authentication (basicAuth):
```python
import time
import ct_ep100_client
from ct_ep100_client.api import alert_api
from ct_ep100_client.model.alert import Alert
from ct_ep100_client.model.error import Error
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
    api_instance = alert_api.AlertApi(api_client)
    alert = Alert(
        mode="webhook",
        dst_ip=[192, 168, 1, 2],
        dst_port=80,
        ftp=AlertFtp(
            active_mode=False,
            add_sub_dir=False,
            user_name="user",
            password="password",
        ),
        path="/notify/tc-kep100",
        timing="bothTriggerReset",
        period_sec=10,
        target=AlertTarget(
            item="co2",
        ),
        condition=AlertCondition(
            direction="rise",
            limit=100.0,
            hysteresis=10.0,
        ),
    ) # Alert |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # アラート設定を1つ登録
        api_response = api_instance.add_alert_setting(alert=alert)
        pprint(api_response)
    except ct_ep100_client.ApiException as e:
        print("Exception when calling AlertApi->add_alert_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**Alert**](Alert.md)|  | [optional]

### Return type

[**Alert**](Alert.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | アラート設定の登録成功 |  * Location - 登録したアラート設定のURL <br>  |
**409** | 登録数の上限に達しているため登録に失敗 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_alert_id_delete**
> alerts_alert_id_delete(alert_id)

指定したidのアラート設定を削除

指定したidのアラート設定を削除する。 

### Example

* Basic Authentication (basicAuth):
```python
import time
import ct_ep100_client
from ct_ep100_client.api import alert_api
from ct_ep100_client.model.error import Error
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
    api_instance = alert_api.AlertApi(api_client)
    alert_id = 0 # int | 取得したいアラート設定のID

    # example passing only required values which don't have defaults set
    try:
        # 指定したidのアラート設定を削除
        api_instance.alerts_alert_id_delete(alert_id)
    except ct_ep100_client.ApiException as e:
        print("Exception when calling AlertApi->alerts_alert_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| 取得したいアラート設定のID |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 指定したidのアラート設定の削除に成功  |  -  |
**404** | 指定したidのアラート設定が存在しない  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_delete**
> alerts_delete()

登録済みアラート設定を全て削除

登録済みアラート設定を全て削除する。   /alerts.html にブラウザからアクセスし操作することも可能 

### Example

* Basic Authentication (basicAuth):
```python
import time
import ct_ep100_client
from ct_ep100_client.api import alert_api
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
    api_instance = alert_api.AlertApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 登録済みアラート設定を全て削除
        api_instance.alerts_delete()
    except ct_ep100_client.ApiException as e:
        print("Exception when calling AlertApi->alerts_delete: %s\n" % e)
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
**204** | アラートの削除に成功   登録済みアラート設定が1つも存在しない場合もこのレスポンスを返す  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_by_id**
> Alert get_alert_by_id(alert_id)

指定したidのアラート設定を取得

### Example

* Basic Authentication (basicAuth):
```python
import time
import ct_ep100_client
from ct_ep100_client.api import alert_api
from ct_ep100_client.model.alert import Alert
from ct_ep100_client.model.error import Error
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
    api_instance = alert_api.AlertApi(api_client)
    alert_id = 1 # int | 取得したいアラート設定のID

    # example passing only required values which don't have defaults set
    try:
        # 指定したidのアラート設定を取得
        api_response = api_instance.get_alert_by_id(alert_id)
        pprint(api_response)
    except ct_ep100_client.ApiException as e:
        print("Exception when calling AlertApi->get_alert_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| 取得したいアラート設定のID |

### Return type

[**Alert**](Alert.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 取得成功 |  -  |
**404** | 登録済みアラート設定が存在しない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> InlineResponse200 get_alerts()

登録済みアラート設定一覧を取得

登録済みのアラートの一覧を取得する。 

### Example

* Basic Authentication (basicAuth):
```python
import time
import ct_ep100_client
from ct_ep100_client.api import alert_api
from ct_ep100_client.model.inline_response200 import InlineResponse200
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
    api_instance = alert_api.AlertApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 登録済みアラート設定一覧を取得
        api_response = api_instance.get_alerts()
        pprint(api_response)
    except ct_ep100_client.ApiException as e:
        print("Exception when calling AlertApi->get_alerts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 取得成功   アラート設定が1つも登録されていなくてもこのレスポンスを返す  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


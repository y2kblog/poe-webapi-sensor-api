# openapi_client.CalibrationApi

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calibration_get**](CalibrationApi.md#calibration_get) | **GET** /calibration | 校正パラメータの取得
[**calibration_put**](CalibrationApi.md#calibration_put) | **PUT** /calibration | 熱電対の校正を実行


# **calibration_get**
> ThermocoupleCalib calibration_get()

校正パラメータの取得

熱電対の校正パラメータを取得する。   /calibration.html にブラウザからアクセスし取得することも可能 

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import calibration_api
from openapi_client.model.thermocouple_calib import ThermocoupleCalib
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
    api_instance = calibration_api.CalibrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # 校正パラメータの取得
        api_response = api_instance.calibration_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CalibrationApi->calibration_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ThermocoupleCalib**](ThermocoupleCalib.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 校正パラメータを応答 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calibration_put**
> ThermocoupleCalib calibration_put()

熱電対の校正を実行

熱電対の校正パラメータを変更する。   /calibration.html にブラウザからアクセスし操作することも可能 

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import calibration_api
from openapi_client.model.thermocouple_calib import ThermocoupleCalib
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
    api_instance = calibration_api.CalibrationApi(api_client)
    thermocouple_calib = ThermocoupleCalib(
        unit="Celsius",
        offset=-0.5,
    ) # ThermocoupleCalib |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 熱電対の校正を実行
        api_response = api_instance.calibration_put(thermocouple_calib=thermocouple_calib)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CalibrationApi->calibration_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thermocouple_calib** | [**ThermocoupleCalib**](ThermocoupleCalib.md)|  | [optional]

### Return type

[**ThermocoupleCalib**](ThermocoupleCalib.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 校正パラメータを応答 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# openapi.api.RawApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rawDelete**](RawApi.md#rawdelete) | **DELETE** /raw | 生値取得終了
[**rawPost**](RawApi.md#rawpost) | **POST** /raw | 生値取得開始
[**rawStatusGet**](RawApi.md#rawstatusget) | **GET** /raw-status | 生値取得状態の取得


# **rawDelete**
> rawDelete()

生値取得終了

時系列音圧データの取得を停止する。   /raw.html にブラウザからアクセスし操作することも可能 

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = RawApi();

try { 
    api_instance.rawDelete();
} catch (e) {
    print('Exception when calling RawApi->rawDelete: $e\n');
}
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rawPost**
> RawSetting rawPost(rawSetting)

生値取得開始

時系列音圧データの取得を開始する。   /raw.html にブラウザからアクセスし操作することも可能   ※送信する音圧データの仕様は以下の\"Callbacks\"タブに記載 

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = RawApi();
final rawSetting = RawSetting(); // RawSetting | 設定用パラメータを指定

try { 
    final result = api_instance.rawPost(rawSetting);
    print(result);
} catch (e) {
    print('Exception when calling RawApi->rawPost: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rawSetting** | [**RawSetting**](RawSetting.md)| 設定用パラメータを指定 | [optional] 

### Return type

[**RawSetting**](RawSetting.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rawStatusGet**
> RawSetting rawStatusGet()

生値取得状態の取得

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = RawApi();

try { 
    final result = api_instance.rawStatusGet();
    print(result);
} catch (e) {
    print('Exception when calling RawApi->rawStatusGet: $e\n');
}
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


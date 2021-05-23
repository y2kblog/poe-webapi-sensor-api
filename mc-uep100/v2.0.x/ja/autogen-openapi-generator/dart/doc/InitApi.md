# openapi.api.InitApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**initPut**](InitApi.md#initput) | **PUT** /init | 製品を初期状態に戻す


# **initPut**
> initPut()

製品を初期状態に戻す

- 生値取得中の場合、生値取得を終了する - ネットワーク設定を初期状態へ戻す   その後、自動的に再起動する   /init.html にブラウザからアクセスし操作することも可能 

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = InitApi();

try { 
    api_instance.initPut();
} catch (e) {
    print('Exception when calling InitApi->initPut: $e\n');
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


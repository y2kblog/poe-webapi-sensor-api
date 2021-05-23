# openapi.api.InfoApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**infoGet**](InfoApi.md#infoget) | **GET** /info | 機器情報の取得
[**infoPatch**](InfoApi.md#infopatch) | **PATCH** /info | 設定変更が可能な機器情報の変更


# **infoGet**
> Info infoGet()

機器情報の取得

機器情報を取得する。   /info.html にブラウザからアクセスし取得することも可能 

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = InfoApi();

try { 
    final result = api_instance.infoGet();
    print(result);
} catch (e) {
    print('Exception when calling InfoApi->infoGet: $e\n');
}
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infoPatch**
> InfoConfigurable infoPatch(infoConfigurable)

設定変更が可能な機器情報の変更

指定したフィールドの値を変更する。   指定されなかったフィールドの値は変更されない。   /info.html にブラウザからアクセスし操作することも可能 

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = InfoApi();
final infoConfigurable = InfoConfigurable(); // InfoConfigurable | 省略したパラメータは変更されない

try { 
    final result = api_instance.infoPatch(infoConfigurable);
    print(result);
} catch (e) {
    print('Exception when calling InfoApi->infoPatch: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infoConfigurable** | [**InfoConfigurable**](InfoConfigurable.md)| 省略したパラメータは変更されない | [optional] 

### Return type

[**InfoConfigurable**](InfoConfigurable.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


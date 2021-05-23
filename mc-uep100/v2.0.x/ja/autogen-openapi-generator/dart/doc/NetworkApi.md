# openapi.api.NetworkApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configNetworkGet**](NetworkApi.md#confignetworkget) | **GET** /config/network | ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得
[**configNetworkPatch**](NetworkApi.md#confignetworkpatch) | **PATCH** /config/network | ネットワーク設定（認証機能・DHCP・手動IP）の変更


# **configNetworkGet**
> NetworkConfig configNetworkGet()

ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得

ネットワーク設定情報を取得する。   初期設定は認証機能：無効、DHCP：有効です。 

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = NetworkApi();

try { 
    final result = api_instance.configNetworkGet();
    print(result);
} catch (e) {
    print('Exception when calling NetworkApi->configNetworkGet: $e\n');
}
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configNetworkPatch**
> NetworkConfig configNetworkPatch(networkConfig)

ネットワーク設定（認証機能・DHCP・手動IP）の変更

指定したフィールドの値を変更する。 指定されなかったフィールドの値は変更されない。   変更に成功した場合、応答後にシステムは自動的に再起動する。   /config/network.html にブラウザからアクセスし操作することも可能 

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = NetworkApi();
final networkConfig = NetworkConfig(); // NetworkConfig | 省略したパラメータは変更されない

try { 
    final result = api_instance.configNetworkPatch(networkConfig);
    print(result);
} catch (e) {
    print('Exception when calling NetworkApi->configNetworkPatch: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkConfig** | [**NetworkConfig**](NetworkConfig.md)| 省略したパラメータは変更されない | [optional] 

### Return type

[**NetworkConfig**](NetworkConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


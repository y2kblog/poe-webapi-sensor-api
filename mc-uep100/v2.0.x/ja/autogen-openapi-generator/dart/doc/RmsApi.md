# openapi.api.RmsApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRms**](RmsApi.md#getrms) | **GET** /rms | 音圧のRMS値を取得


# **getRms**
> RmsResult getRms(lowerFrqHz, upperFrqHz, timeSec)

音圧のRMS値を取得

音圧の実効値を音圧レベル表示した値。   周波数帯域を指定することで、 指定した周波数帯域の音圧の部分オーバーオール値(POA：Partial OverAll)の測定も可能。 

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = RmsApi();
final lowerFrqHz = 1000; // int | 取得する周波数帯域の下限値 (単位：Hz)    <!--省略時：10Hz  --> 
final upperFrqHz = 10000; // int | 取得する周波数帯域の上限値 (単位：Hz)    <!--省略時：80kHz  --> 
final timeSec = 0.5; // double | 測定時間 (単位：sec)   

try { 
    final result = api_instance.getRms(lowerFrqHz, upperFrqHz, timeSec);
    print(result);
} catch (e) {
    print('Exception when calling RmsApi->getRms: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lowerFrqHz** | **int**| 取得する周波数帯域の下限値 (単位：Hz)    <!--省略時：10Hz  -->  | [optional] [default to 10]
 **upperFrqHz** | **int**| 取得する周波数帯域の上限値 (単位：Hz)    <!--省略時：80kHz  -->  | [optional] [default to 80000]
 **timeSec** | **double**| 測定時間 (単位：sec)    | [optional] [default to 0.0256]

### Return type

[**RmsResult**](RmsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


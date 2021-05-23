# openapi.api.NoiseApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://abcdefghik.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNoise**](NoiseApi.md#getnoise) | **GET** /noise | 騒音レベルの取得 


# **getNoise**
> SoundLevelResult getNoise(timeSec, timeWeight)

騒音レベルの取得 

下記3項目を測定する。 周波数重み付け特性はA特性を適用する。  - 等価騒音レベル(Leq)   Equivalent continuous A-weighted sound pressure level.   指定した測定時間内の騒音の総エネルギーの時間平均値を音圧レベル表示した値。   環境騒音の評価量として用いられる。    - 単発騒音暴露レベル(SEL)   Single Event Noise exposure level.   単発的に発生する騒音の全エネルギーと等しいエネルギーを持つ継続時間1秒間の定常音の音圧レベルに換算した値。   単発的または間欠的に発生する継続時間の短い騒音を測定する評価量として用いられる。    - ピーク音圧レベル(Lpeak)   指定した測定時間内の騒音の最大値を音圧レベル表示した値。    ※本製品はJIS C 1509や計量法に定められた騒音計には適合しておりません。 

### Example 
```dart
import 'package:openapi/api.dart';
// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = NoiseApi();
final timeSec = 0.5; // double | 測定時間 (単位：sec)    省略時：0.1024 sec 
final timeWeight = slow; // String | 時間重み付け特性   省略時：Slow   - \"slow\"：時定数1sec。   - \"fast\"：時定数0.125sec。   - \"impulse\"：時定数0.035sec。 

try { 
    final result = api_instance.getNoise(timeSec, timeWeight);
    print(result);
} catch (e) {
    print('Exception when calling NoiseApi->getNoise: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeSec** | **double**| 測定時間 (単位：sec)    省略時：0.1024 sec  | [optional] 
 **timeWeight** | **String**| 時間重み付け特性   省略時：Slow   - \"slow\"：時定数1sec。   - \"fast\"：時定数0.125sec。   - \"impulse\"：時定数0.035sec。  | [optional] [default to 'slow']

### Return type

[**SoundLevelResult**](SoundLevelResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


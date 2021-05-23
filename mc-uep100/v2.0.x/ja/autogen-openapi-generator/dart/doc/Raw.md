# openapi.model.Raw

## Load the model package
```dart
import 'package:openapi/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isRunning** | **bool** | 生値取得状態   falseのとき、他のパラメータは送信されない  | [optional] [readonly] 
**dstIp** | **List<int>** | 送信先IPアドレス   省略時：HTTPリクエストの送信元IP  | [optional] [default to const []]
**dstPort** | **int** | 送信先ポート番号 | 
**frqHz** | **int** | サンプリング周波数 (単位：Hz)    | [optional] [default to RawFrqHzEnum.number160000]
**dataNum** | **int** | データ数   省略時：生値取得終了コマンドを受け取るまでデータを送信し続ける  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



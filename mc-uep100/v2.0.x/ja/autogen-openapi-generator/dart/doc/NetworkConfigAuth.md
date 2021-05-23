# openapi.model.NetworkConfigAuth

## Load the model package
```dart
import 'package:openapi/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | 認証機能の有効/無効  | [optional] [default to false]
**method** | **String** | 認証方式   ※現バージョンではBasic認証のみサポート - \"Basic\"：Basic認証  | [optional] [default to 'Basic']
**userName** | **String** | ユーザ名(最大20文字)  | [optional] 
**password** | **String** | パスワード(最大20文字)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



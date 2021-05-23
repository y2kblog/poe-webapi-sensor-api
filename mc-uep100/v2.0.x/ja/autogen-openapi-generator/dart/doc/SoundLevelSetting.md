# openapi.model.SoundLevelSetting

## Load the model package
```dart
import 'package:openapi/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeSec** | **double** | 測定時間 (単位：sec)    | [optional] 
**timeWeight** | **String** | 時間重み付け特性   省略時：Slow   - \"slow\"：時定数1sec。   - \"fast\"：時定数0.125sec。   - \"impulse\"：時定数0.035sec。  | [optional] [default to 'slow']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



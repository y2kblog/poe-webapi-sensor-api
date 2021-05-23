# openapi.model.InfoConfigurable

## Load the model package
```dart
import 'package:openapi/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customName** | **String** | 設定可能な名称   ユーザが識別を容易にするために利用する。  | [optional] [default to '"customName" is not set']
**blinkLed** | **bool** | Status LED点滅の有無   `false`: デフォルト設定。Status LEDはネットワーク状態に対応した動作を行う   `true`: Status LEDを点滅させる（点灯時間と消灯時間は同一）   本設定は複数のPoE対応WebAPIセンサが設置され製品裏面に記載されたシリアルナンバーを確認できない場合に、どの機器が操作対象であるのかを目視で確認する際に利用する。   ※本設定は電源を再起動するとリセットされる。  | [optional] [default to false]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



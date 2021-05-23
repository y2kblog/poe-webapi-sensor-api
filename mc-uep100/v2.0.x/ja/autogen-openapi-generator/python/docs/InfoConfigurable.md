# InfoConfigurable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_name** | **str** | 設定可能な名称   ユーザが識別を容易にするために利用する。  | [optional]  if omitted the server will use the default value of ""customName" is not set"
**blink_led** | **bool** | Status LED点滅の有無   &#x60;false&#x60;: デフォルト設定。Status LEDはネットワーク状態に対応した動作を行う   &#x60;true&#x60;: Status LEDを点滅させる（点灯時間と消灯時間は同一）   本設定は複数のPoE対応WebAPIセンサが設置され製品裏面に記載されたシリアルナンバーを確認できない場合に、どの機器が操作対象であるのかを目視で確認する際に利用する。   ※本設定は電源を再起動するとリセットされる。  | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



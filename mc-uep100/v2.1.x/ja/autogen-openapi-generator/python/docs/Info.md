# Info


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** | 製品名 | [optional] 
**serial_number** | **str** | 製品シリアル番号 (10桁の半角英小文字) | [optional] 
**mac_address** | **str** | MACアドレス (EUI-48) | [optional] 
**firmware_version** | **str** | ファームウェアのバージョン | [optional] 
**uptime_sec** | **int** | システム稼働時間 (単位：sec) | [optional] 
**custom_name** | **str** | 設定可能な名称   ユーザが識別を容易にするために利用する。  | [optional]  if omitted the server will use the default value of ""customName" is not set"
**blink_led** | **bool** | Status LED点滅の有無   &#x60;false&#x60;: デフォルト設定。Status LEDはネットワーク状態に対応した動作を行う   &#x60;true&#x60;: Status LEDを点滅させる（点灯時間と消灯時間は同一）   本設定は複数のPoE対応WebAPIセンサが設置され製品裏面に記載されたシリアルナンバーを確認できない場合に、どの機器が操作対象であるのかを目視で確認する際に利用する。   ※本設定は電源を再起動するとリセットされる。  | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



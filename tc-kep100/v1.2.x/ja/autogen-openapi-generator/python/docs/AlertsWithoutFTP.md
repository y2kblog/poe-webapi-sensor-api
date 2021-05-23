# AlertsWithoutFTP

アラート設定

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**AlertTarget**](AlertTarget.md) |  | 
**condition** | [**AlertCondition**](AlertCondition.md) |  | 
**alert_id** | **int** | アラートID  | [optional] [readonly] 
**mode** | **str** | 通知モード   省略時：webhook   &#39;webhook&#39;：Webhookモード。アラート情報をHTTPメッセージで通知する。   &#39;ftp&#39;：FTPモード。FTPサーバに対しアラート情報をCSVファイルで保存する。    | [optional] 
**dst_ip** | **[int]** | 送信先IPアドレス（Webhookモード：通知先IPアドレス、FTPモード：FTPサーバのIPアドレス）   省略時：登録時のホストIP   USBからメッセージを受信した場合：通知先IPアドレス設定時はそのIPに対してアラートを送信する。省略時はUSBに対しアラートを送信する。  | [optional] 
**dst_port** | **int** | 送信先ポート番号（Webhookモード：通知先ポート、FTPモード：FTPサーバの制御ポート）   省略時：80（Webhookモード）、21（FTPモード）  | [optional]  if omitted the server will use the default value of 80
**path** | **str** | 送信先パス（Webhookモード：通知先エンドポイント、FTPモード：保存先パス）   省略時：&#39;/notify&#39;（Webhookモード）、&#39;/&#39;（FTPモード）  | [optional]  if omitted the server will use the default value of "/notify"
**timing** | **str** | 通知/保存タイミングの設定   省略時：&#39;bothTriggerReset&#39;   &#39;bothTriggerReset&#39;：アラート発報時およびアラート復帰時（＝アラート状態変化時）に通知   &#39;onlyTrigger&#39;：アラート発報時のみ通知   &#39;eachPeriod&#39;：監視周期毎にアラート状態を継続して通知    | [optional]  if omitted the server will use the default value of "bothTriggerReset"
**period_sec** | **int** | 監視周期 [sec]   省略時：10  | [optional]  if omitted the server will use the default value of 10

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



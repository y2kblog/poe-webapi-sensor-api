# RawSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_port** | **int** | 送信先ポート番号 | 
**is_running** | **bool** | 生値取得状態   falseのとき、他のパラメータは送信されない  | [optional] [readonly] 
**dst_ip** | **[int]** | 送信先IPアドレス   省略時：HTTPリクエストの送信元IP  | [optional] 
**frq_hz** | **int** | サンプリング周波数 (単位：Hz)    | [optional]  if omitted the server will use the default value of 160000
**data_num** | **int** | データ数   省略時：生値取得終了コマンドを受け取るまでデータを送信し続ける  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



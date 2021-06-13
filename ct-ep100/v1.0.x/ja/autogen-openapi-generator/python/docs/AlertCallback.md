# AlertCallback

アラート結果

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** | 製品名 | [optional] 
**serial_number** | **str** | 製品シリアル番号 (10桁の半角英小文字) | [optional] 
**alert_id** | **int** |  | [optional] 
**notify_cnt** | **int** | 通知回数（電源投入時に0にリセットされる）  | [optional] 
**is_triggered** | **bool** | アラート状態   true：アラート発生   false：アラート非発生  | [optional] 
**is_triggered_prev** | **bool** | 1監視周期前のアラート状態   true：アラート発生   false：アラート非発生  | [optional] 
**measured_value** | **float** | 測定値 | [optional] 
**alerts** | [**AlertWithoutFTP**](AlertWithoutFTP.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



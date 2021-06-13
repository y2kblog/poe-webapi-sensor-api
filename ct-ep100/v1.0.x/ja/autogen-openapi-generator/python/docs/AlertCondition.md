# AlertCondition

アラート発生条件の条件設定    - アラート方向：上昇設定時     - アラート発生条件       `測定結果 >= limit`   - アラート復帰条件       `測定結果 < limit - hysteresis`  - アラート方向：下降設定時     - アラート発生条件       `測定結果 <= limit`   - アラート復帰条件       `測定結果 > limit + hysteresis` 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | アラート方向   rise：値の上昇を検知   fall：値の下降を検知  | [optional] 
**limit** | **float** | アラートリミット値  | [optional] 
**hysteresis** | **float** | ヒステリシス値   省略時：0  | [optional]  if omitted the server will use the default value of 0.0

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



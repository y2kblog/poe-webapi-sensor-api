# ConfigCo2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_asc** | **bool** | 自動自己校正機能(ASC: Automatic Self-Calibration)の有効/無効   本設定は製品の電源再投入後も保持されます。    &lt;b&gt;自動自己校正機能に関する注意&lt;/b&gt;   初期の校正パラメータセットを見つけるためには最低7日間の期間が必要です。その間、センサは電源投入状態のまま、毎日最低1時間は新鮮な空気にさらさなければなりません。電源が切られると校正パラメータの検出が中断され、最初からやり直す必要があります。検出に成功すると校正パラメータは不揮発メモリに保存され、再起動後も校正パラメータを利用します。   ASCが常に適切な再校正を行うことができるよう、センサは毎日最低1時間は新鮮な空気にさらされる必要があります。本条件を満たせない場合、ASCを無効化してください。  | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



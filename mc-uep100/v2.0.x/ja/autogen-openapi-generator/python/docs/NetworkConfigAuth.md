# NetworkConfigAuth

認証機能の設定   ※1ユーザのみ設定可 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | 認証機能の有効/無効  | [optional]  if omitted the server will use the default value of False
**method** | **str** | 認証方式   ※現バージョンではBasic認証のみサポート - \&quot;Basic\&quot;：Basic認証  | [optional]  if omitted the server will use the default value of "Basic"
**user_name** | **str** | ユーザ名(最大20文字)  | [optional] 
**password** | **str** | パスワード(最大20文字)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



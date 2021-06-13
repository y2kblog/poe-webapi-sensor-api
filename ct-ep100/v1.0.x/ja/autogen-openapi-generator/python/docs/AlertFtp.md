# AlertFtp

FTP設定。FTPモード時のみ要設定 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_mode** | **bool** | FTPアクティブモード/パッシブモードの選択   true：アクティブモード   false：パッシブモード   省略時：false（パッシブモード）  | [optional]  if omitted the server will use the default value of False
**add_sub_dir** | **bool** | 保存先パスにサブフォルダを作成するかどうかの選択   true：サブフォルダを作成する   false：サブフォルダを作成しない   省略時：false   サブフォルダは&#39;path&#39;で指定されたディレクトリの下に作成される。   &lt;br&gt;**サブフォルダ名の規則**   &#x60;{serialNumber}_xxx&#x60;   xxxxは0埋め3桁の数値（初期値は001）。製品が再起動されるごとに新たなフォルダが連番で作成される。   例：&#39;addSubDir&#39;がtrue、&#39;path&#39;が&#x60;/dir1/dir2&#x60;、&#39;serialNumber&#39;が&#x60;abcdefghij&#x60;のとき、&#x60;/dir1/dir2/abcdefghij_001/&#x60;以下に通知ファイルが保存される  | [optional]  if omitted the server will use the default value of False
**user_name** | **str** | FTPサーバのユーザ名(最大20文字)   ※FTPモード時のみ有効  | [optional] 
**password** | **str** | FTPサーバのパスワード(最大20文字)   ※FTPモード時のみ有効  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



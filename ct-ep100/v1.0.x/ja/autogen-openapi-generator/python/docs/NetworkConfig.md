# NetworkConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**NetworkConfigAuth**](NetworkConfigAuth.md) |  | [optional] 
**dhcp** | [**NetworkConfigDhcp**](NetworkConfigDhcp.md) |  | [optional] 
**enable_mdns** | **bool** | mDNS機能の有効/無効   有効時(true)は \&quot;http://シリアルナンバー.local\&quot; によりアクセス可能  | [optional]  if omitted the server will use the default value of True
**static_ip_address** | **[int]** | 静的IPアドレス (IPv4) | [optional]  if omitted the server will use the default value of [192, 168, 1, 100]
**static_subnet_mask** | **[int]** | 静的サブネットマスク (IPv4) | [optional]  if omitted the server will use the default value of [255, 255, 255, 0]
**static_default_gateway** | **[int]** | 静的デフォルトゲートウェイ (IPv4) | [optional]  if omitted the server will use the default value of [192, 168, 1, 1]
**static_dns_server** | **[int]** | 静的DNSサーバIP (IPv4) | [optional]  if omitted the server will use the default value of [192, 168, 1, 1]
**poe_state** | **bool** | PoE電源状態  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



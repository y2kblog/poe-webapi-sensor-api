# NetworkConfigDhcp

DHCPの設定   

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | DHCPクライアント機能の有効/無効   有効時(true)はDHCPにより自動的にネットワーク設定情報を取得する。   無効時(false)もしくはDHCPでネットワーク設定情報の取得に失敗した場合は staticIpAddress, staticSubnetMask, staticDefaultGateway に設定された静的ネットワーク情報を用いる。  | [optional]  if omitted the server will use the default value of True
**assigned** | **bool** | DHCP割り当て状態   true：DHCPサーバからネットワーク設定情報が割り当て済み   false：DHCPクライアント機能が無効になっているか、まだネットワーク設定情報が割り当てられていない  | [optional] [readonly]  if omitted the server will use the default value of False
**dhcp_ip_address** | **[int]** | 動的IPアドレス (IPv4) dhcpAssignedがtrueのときのみ値が返される  | [optional] [readonly] 
**dhcp_subnet_mask** | **[int]** | 動的サブネットマスク (IPv4) dhcpAssignedがtrueのときのみ値が返される  | [optional] [readonly] 
**dhcp_default_gateway** | **[int]** | 動的デフォルトゲートウェイ (IPv4) dhcpAssignedがtrueのときのみ値が返される  | [optional] [readonly] 
**dhcp_dns_server** | **[int]** | 動的DNSサーバIP (IPv4)   dhcpAssignedがtrueのときのみ値が返される  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



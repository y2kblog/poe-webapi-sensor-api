# openapi.model.NetworkConfig

## Load the model package
```dart
import 'package:openapi/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**NetworkConfigAuth**](NetworkConfigAuth.md) |  | [optional] 
**dhcp** | [**NetworkConfigDhcp**](NetworkConfigDhcp.md) |  | [optional] 
**enableMdns** | **bool** | mDNS機能の有効/無効   有効時(true)は \"http://シリアルナンバー.local\" によりアクセス可能  | [optional] [default to true]
**staticIpAddress** | **List<int>** | 静的IPアドレス (IPv4) | [optional] [default to const []]
**staticSubnetMask** | **List<int>** | 静的サブネットマスク (IPv4) | [optional] [default to const []]
**staticDefaultGateway** | **List<int>** | 静的デフォルトゲートウェイ (IPv4) | [optional] [default to const []]
**staticDnsServer** | **List<int>** | 静的DNSサーバIP (IPv4) | [optional] [default to const []]
**poeState** | **bool** | PoE電源状態  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//
// @dart=2.0

// ignore_for_file: unused_element, unused_import
// ignore_for_file: always_put_required_named_parameters_first
// ignore_for_file: lines_longer_than_80_chars

import 'package:openapi/api.dart';
import 'package:test/test.dart';

// tests for NetworkConfigDhcp
void main() {
  final instance = NetworkConfigDhcp();

  group('test NetworkConfigDhcp', () {
    // DHCPクライアント機能の有効/無効   有効時(true)はDHCPにより自動的にネットワーク設定情報を取得する。   無効時(false)もしくはDHCPでネットワーク設定情報の取得に失敗した場合は staticIpAddress, staticSubnetMask, staticDefaultGateway に設定された静的ネットワーク情報を用いる。 
    // bool enable (default value: true)
    test('to test the property `enable`', () async {
      // TODO
    });

    // DHCP割り当て状態   true：DHCPサーバからネットワーク設定情報が割り当て済み   false：DHCPクライアント機能が無効になっているか、まだネットワーク設定情報が割り当てられていない 
    // bool assigned (default value: false)
    test('to test the property `assigned`', () async {
      // TODO
    });

    // 動的IPアドレス (IPv4) dhcpAssignedがtrueのときのみ値が返される 
    // List<int> dhcpIpAddress (default value: const [])
    test('to test the property `dhcpIpAddress`', () async {
      // TODO
    });

    // 動的サブネットマスク (IPv4) dhcpAssignedがtrueのときのみ値が返される 
    // List<int> dhcpSubnetMask (default value: const [])
    test('to test the property `dhcpSubnetMask`', () async {
      // TODO
    });

    // 動的デフォルトゲートウェイ (IPv4) dhcpAssignedがtrueのときのみ値が返される 
    // List<int> dhcpDefaultGateway (default value: const [])
    test('to test the property `dhcpDefaultGateway`', () async {
      // TODO
    });

    // 動的DNSサーバIP (IPv4)   dhcpAssignedがtrueのときのみ値が返される 
    // List<int> dhcpDnsServer (default value: const [])
    test('to test the property `dhcpDnsServer`', () async {
      // TODO
    });


  });

}

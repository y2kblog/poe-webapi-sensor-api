//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//
// @dart=2.0

// ignore_for_file: unused_element, unused_import
// ignore_for_file: always_put_required_named_parameters_first
// ignore_for_file: lines_longer_than_80_chars

import 'package:openapi/api.dart';
import 'package:test/test.dart';


/// tests for NetworkApi
void main() {
  final instance = NetworkApi();

  group('tests for NetworkApi', () {
    // ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得
    //
    // ネットワーク設定情報を取得する。   初期設定は認証機能：無効、DHCP：有効です。 
    //
    //Future<NetworkConfig> configNetworkGet() async
    test('test configNetworkGet', () async {
      // TODO
    });

    // ネットワーク設定（認証機能・DHCP・手動IP）の変更
    //
    // 指定したフィールドの値を変更する。 指定されなかったフィールドの値は変更されない。   変更に成功した場合、応答後にシステムは自動的に再起動する。   /config/network.html にブラウザからアクセスし操作することも可能 
    //
    //Future<NetworkConfig> configNetworkPatch({ NetworkConfig networkConfig }) async
    test('test configNetworkPatch', () async {
      // TODO
    });

  });
}

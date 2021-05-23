//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//
// @dart=2.0

// ignore_for_file: unused_element, unused_import
// ignore_for_file: always_put_required_named_parameters_first
// ignore_for_file: lines_longer_than_80_chars

import 'package:openapi/api.dart';
import 'package:test/test.dart';

// tests for Info
void main() {
  final instance = Info();

  group('test Info', () {
    // 製品名
    // String productName
    test('to test the property `productName`', () async {
      // TODO
    });

    // 製品シリアル番号 (10桁の半角英小文字)
    // String serialNumber
    test('to test the property `serialNumber`', () async {
      // TODO
    });

    // MACアドレス (EUI-48)
    // String macAddress
    test('to test the property `macAddress`', () async {
      // TODO
    });

    // ファームウェアのバージョン
    // String firmwareVersion
    test('to test the property `firmwareVersion`', () async {
      // TODO
    });

    // システム稼働時間 (単位：sec)
    // int uptimeSec
    test('to test the property `uptimeSec`', () async {
      // TODO
    });

    // 設定可能な名称   ユーザが識別を容易にするために利用する。 
    // String customName (default value: '"customName" is not set')
    test('to test the property `customName`', () async {
      // TODO
    });

    // Status LED点滅の有無   `false`: デフォルト設定。Status LEDはネットワーク状態に対応した動作を行う   `true`: Status LEDを点滅させる（点灯時間と消灯時間は同一）   本設定は複数のPoE対応WebAPIセンサが設置され製品裏面に記載されたシリアルナンバーを確認できない場合に、どの機器が操作対象であるのかを目視で確認する際に利用する。   ※本設定は電源を再起動するとリセットされる。 
    // bool blinkLed (default value: false)
    test('to test the property `blinkLed`', () async {
      // TODO
    });


  });

}

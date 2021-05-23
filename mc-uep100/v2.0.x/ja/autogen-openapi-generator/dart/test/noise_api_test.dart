//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//
// @dart=2.0

// ignore_for_file: unused_element, unused_import
// ignore_for_file: always_put_required_named_parameters_first
// ignore_for_file: lines_longer_than_80_chars

import 'package:openapi/api.dart';
import 'package:test/test.dart';


/// tests for NoiseApi
void main() {
  final instance = NoiseApi();

  group('tests for NoiseApi', () {
    // 騒音レベルの取得 
    //
    // 下記3項目を測定する。 周波数重み付け特性はA特性を適用する。  - 等価騒音レベル(Leq)   Equivalent continuous A-weighted sound pressure level.   指定した測定時間内の騒音の総エネルギーの時間平均値を音圧レベル表示した値。   環境騒音の評価量として用いられる。    - 単発騒音暴露レベル(SEL)   Single Event Noise exposure level.   単発的に発生する騒音の全エネルギーと等しいエネルギーを持つ継続時間1秒間の定常音の音圧レベルに換算した値。   単発的または間欠的に発生する継続時間の短い騒音を測定する評価量として用いられる。    - ピーク音圧レベル(Lpeak)   指定した測定時間内の騒音の最大値を音圧レベル表示した値。    ※本製品はJIS C 1509や計量法に定められた騒音計には適合しておりません。 
    //
    //Future<SoundLevelResult> getNoise({ double timeSec, String timeWeight }) async
    test('test getNoise', () async {
      // TODO
    });

  });
}

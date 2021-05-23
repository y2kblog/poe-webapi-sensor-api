# openapi
\"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。


This Dart package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.x
- Build package: org.openapitools.codegen.languages.DartClientCodegen

## Requirements

Dart 2.0 or later

## Installation & Usage

### Github
If this Dart package is published to Github, add the following dependency to your pubspec.yaml
```
dependencies:
  openapi:
    git: https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```

### Local
To use the package in your local drive, add the following dependency to your pubspec.yaml
```
dependencies:
  openapi:
    path: /path/to/openapi
```

## Tests

TODO

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```dart
import 'package:openapi/api.dart';

// TODO Configure HTTP basic authorization: basicAuth
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').username = 'YOUR_USERNAME'
//defaultApiClient.getAuthentication<HttpBasicAuth>('basicAuth').password = 'YOUR_PASSWORD';

final api_instance = InfoApi();

try {
    final result = api_instance.infoGet();
    print(result);
} catch (e) {
    print('Exception when calling InfoApi->infoGet: $e\n');
}

```

## Documentation for API Endpoints

All URIs are relative to *http://abcdefghik.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InfoApi* | [**infoGet**](doc\/InfoApi.md#infoget) | **GET** /info | 機器情報の取得
*InfoApi* | [**infoPatch**](doc\/InfoApi.md#infopatch) | **PATCH** /info | 設定変更が可能な機器情報の変更
*InitApi* | [**initPut**](doc\/InitApi.md#initput) | **PUT** /init | 製品を初期状態に戻す
*NetworkApi* | [**configNetworkGet**](doc\/NetworkApi.md#confignetworkget) | **GET** /config/network | ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得
*NetworkApi* | [**configNetworkPatch**](doc\/NetworkApi.md#confignetworkpatch) | **PATCH** /config/network | ネットワーク設定（認証機能・DHCP・手動IP）の変更
*NoiseApi* | [**getNoise**](doc\/NoiseApi.md#getnoise) | **GET** /noise | 騒音レベルの取得 
*RawApi* | [**rawDelete**](doc\/RawApi.md#rawdelete) | **DELETE** /raw | 生値取得終了
*RawApi* | [**rawPost**](doc\/RawApi.md#rawpost) | **POST** /raw | 生値取得開始
*RawApi* | [**rawStatusGet**](doc\/RawApi.md#rawstatusget) | **GET** /raw-status | 生値取得状態の取得
*RmsApi* | [**getRms**](doc\/RmsApi.md#getrms) | **GET** /rms | 音圧のRMS値を取得


## Documentation For Models

 - [Error](doc\/Error.md)
 - [ErrorError](doc\/ErrorError.md)
 - [Info](doc\/Info.md)
 - [InfoConfigurable](doc\/InfoConfigurable.md)
 - [NetworkConfig](doc\/NetworkConfig.md)
 - [NetworkConfigAuth](doc\/NetworkConfigAuth.md)
 - [NetworkConfigDhcp](doc\/NetworkConfigDhcp.md)
 - [Noise](doc\/Noise.md)
 - [Raw](doc\/Raw.md)
 - [RawSetting](doc\/RawSetting.md)
 - [Rms](doc\/Rms.md)
 - [RmsResult](doc\/RmsResult.md)
 - [RmsSetting](doc\/RmsSetting.md)
 - [SoundLevelResult](doc\/SoundLevelResult.md)
 - [SoundLevelSetting](doc\/SoundLevelSetting.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP Basic authentication


## Author




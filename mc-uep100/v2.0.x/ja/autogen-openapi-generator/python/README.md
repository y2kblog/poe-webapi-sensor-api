# MC-UEP100-python
\"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.x
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install "git+https://github.com/y2kblog/poe-webapi-sensor-api.git#egg=MC-UEP100-python&subdirectory=mc-uep100/v2.0.x/ja/autogen-openapi-generator/python"
```
(you may need to run `pip` with root permission: `sudo pip install "git+https://github.com/y2kblog/poe-webapi-sensor-api.git#egg=MC-UEP100-python&subdirectory=mc-uep100/v2.0.x/ja/autogen-openapi-generator/python"`)

Then import the package:
```python
import mc_uep100_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mc_uep100_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import mc_uep100_client
from pprint import pprint
from mc_uep100_client.api import info_api
from mc_uep100_client.model.info import Info
from mc_uep100_client.model.info_configurable import InfoConfigurable
# Defining the host is optional and defaults to http://abcdefghik.local
# See configuration.py for a list of all supported configuration parameters.
configuration = mc_uep100_client.Configuration(
    host = "http://abcdefghik.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mc_uep100_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with mc_uep100_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = info_api.InfoApi(api_client)
    
    try:
        # 機器情報の取得
        api_response = api_instance.info_get()
        pprint(api_response)
    except mc_uep100_client.ApiException as e:
        print("Exception when calling InfoApi->info_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://abcdefghik.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InfoApi* | [**info_get**](docs/InfoApi.md#info_get) | **GET** /info | 機器情報の取得
*InfoApi* | [**info_patch**](docs/InfoApi.md#info_patch) | **PATCH** /info | 設定変更が可能な機器情報の変更
*InitApi* | [**init_put**](docs/InitApi.md#init_put) | **PUT** /init | 製品を初期状態に戻す
*NetworkApi* | [**config_network_get**](docs/NetworkApi.md#config_network_get) | **GET** /config/network | ネットワーク設定（認証機能・DHCP・手動IP・PoE）の取得
*NetworkApi* | [**config_network_patch**](docs/NetworkApi.md#config_network_patch) | **PATCH** /config/network | ネットワーク設定（認証機能・DHCP・手動IP）の変更
*NoiseApi* | [**get_noise**](docs/NoiseApi.md#get_noise) | **GET** /noise | 騒音レベルの取得 
*RawApi* | [**raw_delete**](docs/RawApi.md#raw_delete) | **DELETE** /raw | 生値取得終了
*RawApi* | [**raw_post**](docs/RawApi.md#raw_post) | **POST** /raw | 生値取得開始
*RawApi* | [**raw_status_get**](docs/RawApi.md#raw_status_get) | **GET** /raw-status | 生値取得状態の取得
*RmsApi* | [**get_rms**](docs/RmsApi.md#get_rms) | **GET** /rms | 音圧のRMS値を取得


## Documentation For Models

 - [Error](docs/Error.md)
 - [ErrorError](docs/ErrorError.md)
 - [Info](docs/Info.md)
 - [InfoConfigurable](docs/InfoConfigurable.md)
 - [NetworkConfig](docs/NetworkConfig.md)
 - [NetworkConfigAuth](docs/NetworkConfigAuth.md)
 - [NetworkConfigDhcp](docs/NetworkConfigDhcp.md)
 - [Noise](docs/Noise.md)
 - [Raw](docs/Raw.md)
 - [RawSetting](docs/RawSetting.md)
 - [Rms](docs/Rms.md)
 - [RmsResult](docs/RmsResult.md)
 - [RmsSetting](docs/RmsSetting.md)
 - [SoundLevelResult](docs/SoundLevelResult.md)
 - [SoundLevelSetting](docs/SoundLevelSetting.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in mc_uep100_client.apis and mc_uep100_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from mc_uep100_client.api.default_api import DefaultApi`
- `from mc_uep100_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import mc_uep100_client
from mc_uep100_client.apis import *
from mc_uep100_client.models import *
```


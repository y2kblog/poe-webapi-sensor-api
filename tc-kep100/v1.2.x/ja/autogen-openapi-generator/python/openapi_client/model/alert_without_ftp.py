"""
    PoE対応 WebAPI K型熱電対アンプ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 1.2.x
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from openapi_client.model.alert_condition import AlertCondition
    from openapi_client.model.alert_target import AlertTarget
    globals()['AlertCondition'] = AlertCondition
    globals()['AlertTarget'] = AlertTarget


class AlertWithoutFTP(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('mode',): {
            'WEBHOOK': "webhook",
            'FTP': "ftp",
        },
        ('timing',): {
            'BOTHTRIGGERRESET': "bothTriggerReset",
            'ONLYTRIGGER': "onlyTrigger",
            'EACHPERIOD': "eachPeriod",
        },
    }

    validations = {
        ('alert_id',): {
            'inclusive_minimum': 0,
        },
        ('dst_ip',): {
            'max_items': 4,
            'min_items': 4,
        },
        ('dst_port',): {
            'inclusive_minimum': 0,
        },
        ('path',): {
            'max_length': 32,
        },
        ('period_sec',): {
            'inclusive_minimum': 1,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'target': (AlertTarget,),  # noqa: E501
            'condition': (AlertCondition,),  # noqa: E501
            'alert_id': (int,),  # noqa: E501
            'mode': (str,),  # noqa: E501
            'dst_ip': ([int],),  # noqa: E501
            'dst_port': (int,),  # noqa: E501
            'path': (str,),  # noqa: E501
            'timing': (str,),  # noqa: E501
            'period_sec': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'target': 'target',  # noqa: E501
        'condition': 'condition',  # noqa: E501
        'alert_id': 'alertId',  # noqa: E501
        'mode': 'mode',  # noqa: E501
        'dst_ip': 'dstIp',  # noqa: E501
        'dst_port': 'dstPort',  # noqa: E501
        'path': 'path',  # noqa: E501
        'timing': 'timing',  # noqa: E501
        'period_sec': 'periodSec',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, target, condition, *args, **kwargs):  # noqa: E501
        """AlertWithoutFTP - a model defined in OpenAPI

        Args:
            target (AlertTarget):
            condition (AlertCondition):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            alert_id (int): アラートID . [optional]  # noqa: E501
            mode (str): 通知モード   省略時：webhook   'webhook'：Webhookモード。アラート情報をHTTPメッセージで通知する。   'ftp'：FTPモード。FTPサーバに対しアラート情報をCSVファイルで保存する。   . [optional]  # noqa: E501
            dst_ip ([int]): 送信先IPアドレス（Webhookモード：通知先IPアドレス、FTPモード：FTPサーバのIPアドレス）   省略時：登録時のホストIP   USBからメッセージを受信した場合：通知先IPアドレス設定時はそのIPに対してアラートを送信する。省略時はUSBに対しアラートを送信する。 . [optional]  # noqa: E501
            dst_port (int): 送信先ポート番号（Webhookモード：通知先ポート、FTPモード：FTPサーバの制御ポート）   省略時：80（Webhookモード）、21（FTPモード） . [optional] if omitted the server will use the default value of 80  # noqa: E501
            path (str): 送信先パス（Webhookモード：通知先エンドポイント、FTPモード：保存先パス）   省略時：'/notify'（Webhookモード）、'/'（FTPモード） . [optional] if omitted the server will use the default value of "/notify"  # noqa: E501
            timing (str): 通知/保存タイミングの設定   省略時：'bothTriggerReset'   'bothTriggerReset'：アラート発報時およびアラート復帰時（＝アラート状態変化時）に通知   'onlyTrigger'：アラート発報時のみ通知   'eachPeriod'：監視周期毎にアラート状態を継続して通知   . [optional] if omitted the server will use the default value of "bothTriggerReset"  # noqa: E501
            period_sec (int): 監視周期 [sec]   省略時：10 . [optional] if omitted the server will use the default value of 10  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.target = target
        self.condition = condition
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

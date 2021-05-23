# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NetworkConfigDhcp(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enable=True, assigned=False, dhcp_ip_address=None, dhcp_subnet_mask=None, dhcp_default_gateway=None, dhcp_dns_server=None):  # noqa: E501
        """NetworkConfigDhcp - a model defined in OpenAPI

        :param enable: The enable of this NetworkConfigDhcp.  # noqa: E501
        :type enable: bool
        :param assigned: The assigned of this NetworkConfigDhcp.  # noqa: E501
        :type assigned: bool
        :param dhcp_ip_address: The dhcp_ip_address of this NetworkConfigDhcp.  # noqa: E501
        :type dhcp_ip_address: List[int]
        :param dhcp_subnet_mask: The dhcp_subnet_mask of this NetworkConfigDhcp.  # noqa: E501
        :type dhcp_subnet_mask: List[int]
        :param dhcp_default_gateway: The dhcp_default_gateway of this NetworkConfigDhcp.  # noqa: E501
        :type dhcp_default_gateway: List[int]
        :param dhcp_dns_server: The dhcp_dns_server of this NetworkConfigDhcp.  # noqa: E501
        :type dhcp_dns_server: List[int]
        """
        self.openapi_types = {
            'enable': bool,
            'assigned': bool,
            'dhcp_ip_address': List[int],
            'dhcp_subnet_mask': List[int],
            'dhcp_default_gateway': List[int],
            'dhcp_dns_server': List[int]
        }

        self.attribute_map = {
            'enable': 'enable',
            'assigned': 'assigned',
            'dhcp_ip_address': 'dhcpIpAddress',
            'dhcp_subnet_mask': 'dhcpSubnetMask',
            'dhcp_default_gateway': 'dhcpDefaultGateway',
            'dhcp_dns_server': 'dhcpDnsServer'
        }

        self._enable = enable
        self._assigned = assigned
        self._dhcp_ip_address = dhcp_ip_address
        self._dhcp_subnet_mask = dhcp_subnet_mask
        self._dhcp_default_gateway = dhcp_default_gateway
        self._dhcp_dns_server = dhcp_dns_server

    @classmethod
    def from_dict(cls, dikt) -> 'NetworkConfigDhcp':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The networkConfig_dhcp of this NetworkConfigDhcp.  # noqa: E501
        :rtype: NetworkConfigDhcp
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enable(self):
        """Gets the enable of this NetworkConfigDhcp.

        DHCPクライアント機能の有効/無効   有効時(true)はDHCPにより自動的にネットワーク設定情報を取得する。   無効時(false)もしくはDHCPでネットワーク設定情報の取得に失敗した場合は staticIpAddress, staticSubnetMask, staticDefaultGateway に設定された静的ネットワーク情報を用いる。   # noqa: E501

        :return: The enable of this NetworkConfigDhcp.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this NetworkConfigDhcp.

        DHCPクライアント機能の有効/無効   有効時(true)はDHCPにより自動的にネットワーク設定情報を取得する。   無効時(false)もしくはDHCPでネットワーク設定情報の取得に失敗した場合は staticIpAddress, staticSubnetMask, staticDefaultGateway に設定された静的ネットワーク情報を用いる。   # noqa: E501

        :param enable: The enable of this NetworkConfigDhcp.
        :type enable: bool
        """

        self._enable = enable

    @property
    def assigned(self):
        """Gets the assigned of this NetworkConfigDhcp.

        DHCP割り当て状態   true：DHCPサーバからネットワーク設定情報が割り当て済み   false：DHCPクライアント機能が無効になっているか、まだネットワーク設定情報が割り当てられていない   # noqa: E501

        :return: The assigned of this NetworkConfigDhcp.
        :rtype: bool
        """
        return self._assigned

    @assigned.setter
    def assigned(self, assigned):
        """Sets the assigned of this NetworkConfigDhcp.

        DHCP割り当て状態   true：DHCPサーバからネットワーク設定情報が割り当て済み   false：DHCPクライアント機能が無効になっているか、まだネットワーク設定情報が割り当てられていない   # noqa: E501

        :param assigned: The assigned of this NetworkConfigDhcp.
        :type assigned: bool
        """

        self._assigned = assigned

    @property
    def dhcp_ip_address(self):
        """Gets the dhcp_ip_address of this NetworkConfigDhcp.

        動的IPアドレス (IPv4) dhcpAssignedがtrueのときのみ値が返される   # noqa: E501

        :return: The dhcp_ip_address of this NetworkConfigDhcp.
        :rtype: List[int]
        """
        return self._dhcp_ip_address

    @dhcp_ip_address.setter
    def dhcp_ip_address(self, dhcp_ip_address):
        """Sets the dhcp_ip_address of this NetworkConfigDhcp.

        動的IPアドレス (IPv4) dhcpAssignedがtrueのときのみ値が返される   # noqa: E501

        :param dhcp_ip_address: The dhcp_ip_address of this NetworkConfigDhcp.
        :type dhcp_ip_address: List[int]
        """
        if dhcp_ip_address is not None and len(dhcp_ip_address) > 4:
            raise ValueError("Invalid value for `dhcp_ip_address`, number of items must be less than or equal to `4`")  # noqa: E501
        if dhcp_ip_address is not None and len(dhcp_ip_address) < 4:
            raise ValueError("Invalid value for `dhcp_ip_address`, number of items must be greater than or equal to `4`")  # noqa: E501

        self._dhcp_ip_address = dhcp_ip_address

    @property
    def dhcp_subnet_mask(self):
        """Gets the dhcp_subnet_mask of this NetworkConfigDhcp.

        動的サブネットマスク (IPv4) dhcpAssignedがtrueのときのみ値が返される   # noqa: E501

        :return: The dhcp_subnet_mask of this NetworkConfigDhcp.
        :rtype: List[int]
        """
        return self._dhcp_subnet_mask

    @dhcp_subnet_mask.setter
    def dhcp_subnet_mask(self, dhcp_subnet_mask):
        """Sets the dhcp_subnet_mask of this NetworkConfigDhcp.

        動的サブネットマスク (IPv4) dhcpAssignedがtrueのときのみ値が返される   # noqa: E501

        :param dhcp_subnet_mask: The dhcp_subnet_mask of this NetworkConfigDhcp.
        :type dhcp_subnet_mask: List[int]
        """
        if dhcp_subnet_mask is not None and len(dhcp_subnet_mask) > 4:
            raise ValueError("Invalid value for `dhcp_subnet_mask`, number of items must be less than or equal to `4`")  # noqa: E501
        if dhcp_subnet_mask is not None and len(dhcp_subnet_mask) < 4:
            raise ValueError("Invalid value for `dhcp_subnet_mask`, number of items must be greater than or equal to `4`")  # noqa: E501

        self._dhcp_subnet_mask = dhcp_subnet_mask

    @property
    def dhcp_default_gateway(self):
        """Gets the dhcp_default_gateway of this NetworkConfigDhcp.

        動的デフォルトゲートウェイ (IPv4) dhcpAssignedがtrueのときのみ値が返される   # noqa: E501

        :return: The dhcp_default_gateway of this NetworkConfigDhcp.
        :rtype: List[int]
        """
        return self._dhcp_default_gateway

    @dhcp_default_gateway.setter
    def dhcp_default_gateway(self, dhcp_default_gateway):
        """Sets the dhcp_default_gateway of this NetworkConfigDhcp.

        動的デフォルトゲートウェイ (IPv4) dhcpAssignedがtrueのときのみ値が返される   # noqa: E501

        :param dhcp_default_gateway: The dhcp_default_gateway of this NetworkConfigDhcp.
        :type dhcp_default_gateway: List[int]
        """
        if dhcp_default_gateway is not None and len(dhcp_default_gateway) > 4:
            raise ValueError("Invalid value for `dhcp_default_gateway`, number of items must be less than or equal to `4`")  # noqa: E501
        if dhcp_default_gateway is not None and len(dhcp_default_gateway) < 4:
            raise ValueError("Invalid value for `dhcp_default_gateway`, number of items must be greater than or equal to `4`")  # noqa: E501

        self._dhcp_default_gateway = dhcp_default_gateway

    @property
    def dhcp_dns_server(self):
        """Gets the dhcp_dns_server of this NetworkConfigDhcp.

        動的DNSサーバIP (IPv4)   dhcpAssignedがtrueのときのみ値が返される   # noqa: E501

        :return: The dhcp_dns_server of this NetworkConfigDhcp.
        :rtype: List[int]
        """
        return self._dhcp_dns_server

    @dhcp_dns_server.setter
    def dhcp_dns_server(self, dhcp_dns_server):
        """Sets the dhcp_dns_server of this NetworkConfigDhcp.

        動的DNSサーバIP (IPv4)   dhcpAssignedがtrueのときのみ値が返される   # noqa: E501

        :param dhcp_dns_server: The dhcp_dns_server of this NetworkConfigDhcp.
        :type dhcp_dns_server: List[int]
        """
        if dhcp_dns_server is not None and len(dhcp_dns_server) > 4:
            raise ValueError("Invalid value for `dhcp_dns_server`, number of items must be less than or equal to `4`")  # noqa: E501
        if dhcp_dns_server is not None and len(dhcp_dns_server) < 4:
            raise ValueError("Invalid value for `dhcp_dns_server`, number of items must be greater than or equal to `4`")  # noqa: E501

        self._dhcp_dns_server = dhcp_dns_server

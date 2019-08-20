#
# -*- coding: utf-8 -*-
# Copyright 2019 Fortinet, Inc.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the nxos_interfaces module
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type


class FirewallArgs(object):
    """The arg spec for the fortios_monitor module
    """

    def __init__(self, **kwargs):
        pass

    firewall_policy_select_spec = {
        "firewall_policy_select": {
            "required": False, "type": "dict",
            "options": {
                "policyid": {"required": False, "type": "int"},
            }
        }
    }
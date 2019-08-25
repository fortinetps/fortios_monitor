#
# -*- coding: utf-8 -*-
# Copyright 2019 Fortinet, Inc.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the fortios_facts module
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type


class UserArgs(object):
    """The arg spec for the fortios_facts module
    """

    def __init__(self, **kwargs):
        pass

    user_device_select_spec = {
        "user_device_select": {
            "required": False, "type": "dict",
            "options": {
                "master_only": {"required": False, "type": "bool"},
                "compliance_visibility": {"required": False, "type": "bool"},
                "intf_name": {"required": False, "type": "str"},
                "master_mac": {"required": False, "type": "str"}
            }
        }
    }
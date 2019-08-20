#
# -*- coding: utf-8 -*-
# Copyright 2019 Fortinet, Inc.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the nxos_lacp module
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type


class SystemArgs(object):
    """The arg spec for the fortios_monitor module
    """

    def __init__(self, **kwargs):
        pass

    system_config_backup_spec = {
        "system_config_backup": {
            "required": False, "type": "dict",
            "options": {
                "destination": {"required": False, "type": "str",
                                "choices": ["file", "usb"]},
                "filename": {"required": False, "type": "str"},
                "password": {"required": False, "type": "str"},
                "scope": {"required": True, "type": "str",
                          "choices": ["global", "vdom"]},
                "usb_filename": {"required": False, "type": "str"},
                "vdom": {"required": False, "type": "str"}
            }
        }
    }

    system_current_admins_select_spec = {
        "system_current_admins_select": {
            "required": False, "type": "dict",
            "options": {
                
            }
        }
    }

    system_firmware_upgrade_spec = {
        "system_firmware_upgrade": {
            "required": False, "type": "dict",
            "options": {
                "file_content": {"required": False, "type": "str"},
                "filename": {"required": False, "type": "str"},
                "format_partition": {"required": False, "type": "bool"},
                "source": {"required": True, "type": "str",
                            "choices": ["upload", "usb", "fortiguard"]}
            }
        }
    }

    system_interface_select_spec = {
        "system_interface_select": {
            "required": False, "type": "dict",
             "options": {
                 "interface_name": {"required": False, "type": "str"},
                 "include_vlan": {"required": False, "type": "bool"}
             }
        }
    }

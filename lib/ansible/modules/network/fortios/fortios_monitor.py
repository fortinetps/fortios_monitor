#!/usr/bin/python
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}


DOCUMENTATION = """
---
module: fortios_monitor
extends_documentation_fragment: fortios
version_added: "2.9"
short_description: Gets facts about NX-OS switches
description:
  - Collects facts from Cisco Nexus devices running the NX-OS operating
    system.  Fact collection is supported over both Cli and Nxapi
    transports.  This module prepends all of the base network fact keys
    with C(ansible_net_<fact>).  The facts module will always collect a
    base set of facts from the device and can enable or disable
    collection of additional facts.
author:
  - Jason Edelman (@jedelman8)
  - Gabriele Gerbino (@GGabriele)
notes:
  - Tested against fortios 6.0.2 on FortiGate-VM
options:
  gather_network_resources:
    description:
      - When supplied, this argument will restrict the facts collected
        to a given subset. Possible values for this argument include
        all and the resources like interfaces, vlans etc.
        Can specify a list of values to include a larger subset.
    choices: ['all', 'lag_interfaces', 'telemetry', 'vlans', 'lacp', 'lacp_interfaces', 'interfaces']
    required: false
    version_added: "2.9"
"""

EXAMPLES = """
- name: Gather resource facts
  fortios_monitor:
    gather_network_resources: all

- name: Gather only the interfaces resource facts
  fortios_monitor:
    gather_network_resources:
      - interfaces

- name: Gather interfaces resource
  fortios_monitor:
    gather_network_resources: interfaces
"""

RETURN = """
ansible_net_gather_network_resources:
  description: The list of fact for network resource subsets collected from the device
  returned: when the resource is configured
  type: list

# default
ansible_net_model:
  description: The model name returned from the device
  returned: always
  type: str
ansible_net_serialnum:
  description: The serial number of the remote device
  returned: always
  type: str
ansible_net_version:
  description: The operating system version running on the remote device
  returned: always
  type: str
ansible_net_hostname:
  description: The configured hostname of the device
  returned: always
  type: str
ansible_net_image:
  description: The image file the device is running
  returned: always
  type: str
ansible_net_api:
  description: The name of the transport
  returned: always
  type: str
ansible_net_license_hostid:
  description: The License host id of the device
  returned: always
  type: str
ansible_net_python_version:
  description: The Python version Ansible controller is using
  returned: always
  type: str

# hardware
ansible_net_filesystems:
  description: All file system names available on the device
  returned: when hardware is configured
  type: list
ansible_net_memfree_mb:
  description: The available free memory on the remote device in Mb
  returned: when hardware is configured
  type: int
ansible_net_memtotal_mb:
  description: The total memory on the remote device in Mb
  returned: when hardware is configured
  type: int

# config
ansible_net_config:
  description: The current active config from the device
  returned: when config is configured
  type: str

# interfaces
ansible_net_all_ipv4_addresses:
  description: All IPv4 addresses configured on the device
  returned: when interfaces is configured
  type: list
ansible_net_all_ipv6_addresses:
  description: All IPv6 addresses configured on the device
  returned: when interfaces is configured
  type: list
ansible_net_interfaces:
  description: A hash of all interfaces running on the system
  returned: when interfaces is configured
  type: dict
ansible_net_neighbors:
  description:
    - The list of LLDP and CDP neighbors from the device. If both,
      CDP and LLDP neighbor data is present on one port, CDP is preferred.
  returned: when interfaces is configured
  type: dict

# legacy (pre Ansible 2.2)
fan_info:
  description: A hash of facts about fans in the remote device
  returned: when legacy is configured
  type: dict
hostname:
  description: The configured hostname of the remote device
  returned: when legacy is configured
  type: dict
interfaces_list:
  description: The list of interface names on the remote device
  returned: when legacy is configured
  type: dict
kickstart:
  description: The software version used to boot the system
  returned: when legacy is configured
  type: str
module:
  description: A hash of facts about the modules in a remote device
  returned: when legacy is configured
  type: dict
platform:
  description: The hardware platform reported by the remote device
  returned: when legacy is configured
  type: str
power_supply_info:
  description: A hash of facts about the power supplies in the remote device
  returned: when legacy is configured
  type: str
vlan_list:
  description: The list of VLAN IDs configured on the remote device
  returned: when legacy is configured
  type: list
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.fortios.argspec.facts.facts import FactsArgs
from ansible.module_utils.network.fortios.argspec.system.system import *
from ansible.module_utils.network.fortios.argspec.firewall.firewall import *
from ansible.module_utils.network.fortios.facts.facts import Facts
from fortiosapi import FortiOSAPI


def login(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']
    ssl_verify = data['ssl_verify']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password, verify=ssl_verify)


def main():
    """ Main entry point for AnsibleModule
    """
    argument_spec = FactsArgs.argument_spec
    argument_spec.update(SystemArgs.system_firmware_upgrade_spec)
    argument_spec.update(SystemArgs.system_interface_select_spec)

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=False)

    warnings = []

    fos = FortiOSAPI()
    login(module.params, fos)
    module._connection = fos

    result = Facts(module, fos).get_facts()

    ansible_facts, additional_warnings = result
    warnings.extend(additional_warnings)

    module.exit_json(ansible_facts=ansible_facts, warnings=warnings)


if __name__ == '__main__':
    main()
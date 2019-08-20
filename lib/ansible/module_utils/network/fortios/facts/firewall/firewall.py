#
# -*- coding: utf-8 -*-
# Copyright 2019 Fortinet, Inc.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The fortios firewall monitor class
It is in this file the runtime information is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import re
from copy import deepcopy

from ansible.module_utils.network.common import utils
from ansible.module_utils.network.fortios.argspec.firewall.firewall import FirewallArgs


class FirewallFacts(object):
    """ The fortios firewall fact class
    """

    def __init__(self, module, fos, uri=None, subspec='config', options='options'):
        self._module = module
        self._fos = fos
        self._uri = uri
        self.argument_spec = FirewallArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for firewall
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        obj = []
        if not data:
            data = connection.get("show running-config | include system")
        resources = data.strip()
        objs = self.render_config(self.generated_spec, resources)
        ansible_facts['ansible_network_resources'].pop('system', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['system'] = utils.remove_empties(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts


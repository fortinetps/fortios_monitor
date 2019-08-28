export ansible_lib="/usr/local/lib/python3.7/site-packages/ansible"
export ansible_dev_lib="/workspaces/ansible/lib/ansible"
export ansible_dev_test="/workspaces/ansible/test"

cp -r /workspaces/fortios_monitor/lib/ansible/* $ansible_lib/
cp -r /workspaces/fortios_monitor/lib/ansible/* $ansible_dev_lib/
cp -r /workspaces/fortios_monitor/test/* $ansible_dev_test/

ls -l $ansible_lib/modules/network/fortios/fortios_facts.py
ls -lR $ansible_lib/module_utils/network/fortios/argspec/*
ls -lR $ansible_lib/module_utils/network/fortios/facts/*

ls -l $ansible_dev_lib/modules/network/fortios/fortios_facts.py
ls -lR $ansible_dev_lib/module_utils/network/fortios/argspec/*
ls -lR $ansible_dev_lib/module_utils/network/fortios/facts/*

ls -lR $ansible_dev_test/units/modules/network/fortios/test_fortios_facts.py

# code $ansible_lib/modules/network/fortios/fortios_facts.py
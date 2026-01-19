#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: set_custom_facts
short_description: Set custom facts from host variables
description:
    - Takes host variables and explicitly sets them as ansible facts
    - Useful for deduplication testing where we need specific fact values
options:
    ansible_product_serial:
        description: Product serial number to set as fact
        required: false
        type: str
    ansible_machine_id:
        description: Machine ID to set as fact
        required: false
        type: str
'''

def main():
    module = AnsibleModule(
        argument_spec=dict(
            ansible_product_serial=dict(type='str', required=False),
            ansible_machine_id=dict(type='str', required=False),
        ),
        supports_check_mode=True
    )

    facts = {}
    
    if module.params['ansible_product_serial']:
        facts['ansible_product_serial'] = module.params['ansible_product_serial']
    
    if module.params['ansible_machine_id']:
        facts['ansible_machine_id'] = module.params['ansible_machine_id']

    module.exit_json(changed=False, ansible_facts=facts)

if __name__ == '__main__':
    main()

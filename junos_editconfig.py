#!/usr/bin/env python3

from ncclient import manager
from lxml import etree
from ncclient.operations.rpc import RPCError


def main():
    with manager.connect(host='<MY IP ADDRESS>',
                         port=830,
                         username='<MY USERNAME>',
                         password='<MY PASSWORD>',
                         hostkey_verify=False,
                         device_params={'name': 'junos'},
                         allow_agent=False,
                         look_for_keys=False
                         ) as junos_nc:

        

        cfg1 = '''
             <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
             
            <MY XML CONFIG>


           </nc:config>
             '''
        try:
            resp = junos_nc.edit_config(cfg1, target='candidate',
                                             default_operation='merge')
            
            print(resp)
            print('*' * 30)
        except RPCError as err:
            for attr in dir(err):
                if not attr.startswith('__'):
                    print(attr, ':   ', getattr(err, attr))


if __name__ == '__main__':
    main()

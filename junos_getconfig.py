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

        f1 = '''
         
        <MY XML FILTER>

        '''

       
       
       

        try:
            oc_resp = junos_nc.get_config('running',
                                               filter=('subtree', f1))
            print(oc_resp)
            print('*' * 30)
        except RPCError as err:
            for attr in dir(err):
                print(attr, ':   ', getattr(err, attr))


if __name__ == '__main__':
    main()

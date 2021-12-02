from routerconfigbinding import routerconfig
import pyangbind.lib.pybindJSON as pybindJSON

router1 = routerconfig()



router1.router.interfaces.interface.add('GigabitEthernet 0/0')
router1.router.interfaces.interface['GigabitEthernet 0/0'].speed = 1000
router1.router.interfaces.interface.add('GigabitEthernet 0/1')
router1.router.interfaces.interface['GigabitEthernet 0/1'].ipaddress = '10.10.1.1'
router1.router.interfaces.interface['GigabitEthernet 0/1'].adminup = True

router1.router.ospf.area.add('0')
router1.router.ospf.area['0'].interface = ['GigabitEthernet 0/0']


print(pybindJSON.dumps(router1))

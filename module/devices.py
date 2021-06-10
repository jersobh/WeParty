import pytun


class ServerVirtualDevice:

    def __init__(self, tname='srv-tap0', taddr='192.168.1.40', tmask='255.255.255.0', tmtu=1500):
        self._tun = pytun.TunTapDevice(name=tname, flags=pytun.IFF_TUN | pytun.IFF_NO_PI)
        self._tun.addr = taddr
        self._tun.netmask = tmask
        self._tun.mtu = tmtu
        self._tun.up()

    def get_device(self):
        return self._tun


class ClientVirtualDevice:

    def __init__(self, tname='cli-tap0', taddr='192.168.1.10', tmask='255.255.255.0', tmtu=1500):
        self._tun = pytun.TunTapDevice(name=tname, flags=pytun.IFF_TUN | pytun.IFF_NO_PI)
        self._tun.addr = taddr
        self._tun.netmask = tmask
        self._tun.mtu = tmtu
        self._tun.up()

    def get_device(self):
        return self._tun

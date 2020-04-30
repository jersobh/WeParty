from tuntap import TunTap


class ServerVirtualDevice:

    def __init__(self):
        self.tap = TunTap(nic_type="Tap", nic_name='srv-tap0')
        self.tap.config(ip="192.168.1.10", mask="255.255.255.240", gateway="192.168.1.10")

    def get_device(self):
        try:
            return self.tap
        except Exception as error:
            print(error)
            return f'Error while creating device: {error}'


class ClientVirtualDevice:

    def __init__(self):
        self.tap = TunTap(nic_type="Tap", nic_name='cli-tap1')
        self.tap.config(ip="192.168.1.12", mask="255.255.255.240", gateway="192.168.1.10")

    def get_device(self):
        try:
            return self.tap
        except Exception as error:
            print(error)
            return f'Error while creating device: {error}'
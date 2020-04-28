from tuntap import TunTap


class VirtualDevice:
    
    @staticmethod
    def create(network_name):
        try:
            tap = TunTap(nic_type="Tap", nic_name=network_name)
            tap.config(ip="192.168.1.10", mask="255.255.255.0", gateway="192.168.1.254")
        except Exception as error:
            print(error)
            pass
        finally:
            return 'Device created'


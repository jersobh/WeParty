import asyncio
import json
import threading
from module.devices import ClientVirtualDevice

from autobahn.asyncio.websocket import WebSocketClientProtocol, \
    WebSocketClientFactory


class MyClientProtocol(WebSocketClientProtocol):

    def __init__(self):
        super().__init__()
        self.virtual_device = ClientVirtualDevice(taddr='192.168.1.3')
        self.device = self.virtual_device.get_device()
        self.b = None

    def listen_tap(self):
        while True:
            data = self.device.read(1500)
            print(data)
            self.sendMessage(data, isBinary=True)

    def onConnect(self, response):
        self.b = threading.Thread(name='background', target=factory.protocol.listen_tap(self))
        self.b.start()
        print("Server connected: {0}".format(response.peer))

    def onConnecting(self, transport_details):
        print("Connecting; transport details: {}".format(transport_details))
        return None  # ask for defaults

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            self.device.write(payload)
        else:
            pass

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


if __name__ == '__main__':
    factory = WebSocketClientFactory("ws://191.185.9.20:9000")
    factory.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_connection(factory, '191.185.9.20', 9000)
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
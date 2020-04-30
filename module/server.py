import asyncio
import uvloop
from module.devices import ServerVirtualDevice
import threading
import json

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from autobahn.asyncio.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory


class MyServerFactory(WebSocketServerFactory):
    def __init__(self):
        WebSocketServerFactory.__init__(self, "ws://127.0.0.1:9000")
        self.clients = set()
        self.virtual_device = ServerVirtualDevice()
        self.device = self.virtual_device.get_device()

    def listen_tap(self):
        while True:
            data = self.device.read(1500)
            print(data)
            self.broadcast(data, True)

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            self.clients.add(client)

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, payload, isBinary):
        # if isBinary:
            # print("Binary message received: {0} bytes".format(len(payload)))
        # else:
            # print("Text message received: {0}".format(payload.decode('utf8')))

        for c in self.clients:
            # c.sendMessage(msg.encode('utf8'))
            c.sendMessage(payload, isBinary)


class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")
        self.factory.register(self)
        print(self.factory.clients)

    def onMessage(self, payload, isBinary):
        if isBinary:
            print(payload)
            self.factory.device.write(payload)
            self.factory.broadcast(payload, isBinary)
        else:
            data = json.loads(payload.decode('utf8'))
            print("Text message received: {0}".format(payload.decode('utf8')))



    def onClose(self, wasClean, code, reason):
        self.factory.unregister(self)
        print("WebSocket connection closed: {0}".format(reason))


if __name__ == '__main__':
    factory = MyServerFactory()
    factory.protocol = MyServerProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '0.0.0.0', 9000)
    server = loop.run_until_complete(coro)

    try:
        b = threading.Thread(name='background', target=factory.listen_tap)
        b.start()
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()

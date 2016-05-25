import asyncio

class Server(asyncio.Protocol):
    def __init__(self):
        self.game = ''

    def data_received(self, data):        
        self.transport.write("You:".encode())
        self.transport.write(data)
        self.transport.write("Everyone:".encode())
        self.transport.write(self.game.encode())
        self.transport.close()
        self.game += data.decode()

    def connection_made(self, transport):
        self.transport = transport

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    srv = loop.create_server(Server, host='localhost', port=11111, reuse_address=True)
    loop.run_until_complete(srv)
    loop.run_forever()

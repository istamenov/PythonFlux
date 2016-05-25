import asyncio

class Server(asyncio.Protocol):
    def __init__(self, loop):
        self.game = ''.encode()
        server = loop.create_server(Server, host='localhost', port=11111, reuse_address=True)
        loop.run_until_complete(server)

    def data_received(self, data):        
        self.transport.write("You:".encode())
        self.transport.write(turn)
        self.transport.write("Everyone:".encode())
        self.transport.write(self.game)
        self.game.append(turn)
        self.transport.close()

    def connection_made(self, transport):
        self.transport = transport

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    Server(loop)
    loop.run_forever()

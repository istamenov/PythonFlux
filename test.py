import unittest
import asyncio
import server
try:
    from socket import socketpair
except ImportError:
    from asyncio.windows_utils import socketpair

class MyProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.transport.write("ha-ha".encode())
    
    def data_received(self, data):
        print("Received:", data.decode())
        self.transport.close()

class TestAsync(unittest.TestCase):
    def test_client(self):
        loop = asyncio.get_event_loop()
        server.Server(loop)
        connect = loop.create_connection(MyProtocol, host='localhost', port=11111)
        loop.run_until_complete(connect)
        loop.run_forever()
        
if __name__ == '__main__':
    unittest.main()

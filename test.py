import unittest
import asyncio
import server

class Client(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.transport.write("ha-ha".encode())

    def data_received(self, data):
        self.data = data.decode()
        self.transport.close()
        asyncio.get_event_loop().stop()

class TestAsync(unittest.TestCase):
    def test_client(self):
        loop = asyncio.get_event_loop()
        srv = loop.create_server(server.Server, host='localhost', port=11111, reuse_address=True)
        asyncio.ensure_future(srv)
        client = Client()
        connect = loop.create_connection(lambda: client, host='localhost', port=11111)
        asyncio.ensure_future(connect)
        loop.run_forever()
        loop.close()
        self.assertEqual(client.data, "You:ha-haEveryone:")

if __name__ == '__main__':
    unittest.main(warnings='ignore')

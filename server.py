from twisted.internet import protocol, reactor
from config import service

import logging
logging.basicConfig(filename='server.log', filemode='a', level=logging.DEBUG)

class Duck(protocol.Protocol):
    def dataReceived(self, data):
        if data.rstrip('\r\n') == 'exit':
            self.transport.write('quack bye...')
            self.transport.loseConnection()
        elif data.rstrip('\r\n') == 'quack':
            self.transport.write('yeah, quack too!')
        else:
            self.transport.write(data)

class DuckFactory(protocol.Factory):
    def buildProtocol(self, addr):
        logging.info('Connection from %s', addr)
        return Duck()

def run():
    reactor.listenTCP(service['port'], DuckFactory())
    reactor.run()

if __name__ == '__main__':
    run()

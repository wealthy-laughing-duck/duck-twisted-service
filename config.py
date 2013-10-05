import os, ConfigParser

c = ConfigParser.ConfigParser()
c.read(os.path.abspath('./config.ini'))

service = {'port': c.getint('service', 'port')}

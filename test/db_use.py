#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
logging.getLogger().setLevel('DEBUG')

###############
# settings.py #
###############
connections_opts = {
    'mongodb': {
        'core': {
            'enable': True,
            'host': '127.0.0.1',
            'port': 27017,
            'username': None,
            'password': None,
            'keep_time': 7200,
        }
    }
}


###############
# __init__.py #
###############

from torext.db.connections import Connections
connections = Connections.instance(connections_opts)

print connections

mdb = connections.get('mongodb', 'core')
print mdb

#############
# models.py #
#############

from torext.db.mongodb import *

class CollectionDeclarer(CollectionDeclarer):
    connection = connections.get('mongodb', 'core')

class TestDoc(Document):
    col = CollectionDeclarer('test', 'col0')
    __id_map__ = True
    struct = {
        'id': ObjectId,
        'name': str,
        'age': int,
    }

td = TestDoc.new()

print td

td.save()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
"""

"""

from wsco.client import SocketClient
from wsco.constants import Constants



def test_init():
    s = SocketClient()
    assert s.host == Constants.HOST
    assert s.port == Constants.PORT

    host = '127.0.0.1'
    port = 54321
    s = SocketClient(host = host, port = port)
    assert s.host == host
    assert s.port == port

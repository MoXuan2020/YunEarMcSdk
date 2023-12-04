# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi


class YunEarMcSdkServer(serverApi.GetServerSystemCls(), object):

    def __init__(self, namespace, systemName):
        super(YunEarMcSdkServer, self).__init__(namespace, systemName)

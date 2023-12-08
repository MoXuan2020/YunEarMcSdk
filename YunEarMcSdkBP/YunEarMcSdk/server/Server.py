# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi

ServerSystemCls = serverApi.GetServerSystemCls()


class YunEarMcSdkServer(ServerSystemCls, object):

    def __init__(self, namespace, systemName):
        super(YunEarMcSdkServer, self).__init__(namespace, systemName)

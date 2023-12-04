# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi


class YunEarMcSdkClient(clientApi.GetClientSystemCls(), object):

    def __init__(self, namespace, systemName):
        super(YunEarMcSdkClient, self).__init__(namespace, systemName)

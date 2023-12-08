# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi

ClientSystemCls = clientApi.GetClientSystemCls()


class YunEarMcSdkClient(ClientSystemCls, object):

    def __init__(self, namespace, systemName):
        super(YunEarMcSdkClient, self).__init__(namespace, systemName)

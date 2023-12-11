# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi

ScreenNodeCls = clientApi.GetScreenNodeCls()


class MobEditorScreenNode(ScreenNodeCls, object):

    def __init__(self, namespace, name, param):
        super(MobEditorScreenNode, self).__init__(namespace, name, param)

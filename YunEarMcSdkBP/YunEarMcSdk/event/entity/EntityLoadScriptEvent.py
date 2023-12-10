# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityLoadScriptEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityLoadScriptEvent, self).__init__(callback)
        self.args_ = None

    def CreateFromArgs(self, args):
        self.args_ = args["args"]

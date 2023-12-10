# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityLoadScriptEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityLoadScriptEvent, self).__init__(callback)
        self.args = None

    def CreateFromArgs(self, args):
        self.args = args.get("args")

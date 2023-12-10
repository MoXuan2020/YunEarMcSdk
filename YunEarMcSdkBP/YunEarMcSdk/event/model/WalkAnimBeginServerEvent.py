# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class WalkAnimBeginServerEvent(ServerEvent):

    def __init__(self, callback):
        super(WalkAnimBeginServerEvent, self).__init__(callback)
        self.id_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]

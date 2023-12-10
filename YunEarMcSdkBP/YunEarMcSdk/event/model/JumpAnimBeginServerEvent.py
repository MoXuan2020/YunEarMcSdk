# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class JumpAnimBeginServerEvent(ServerEvent):

    def __init__(self, callback):
        super(JumpAnimBeginServerEvent, self).__init__(callback)
        self.id_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]

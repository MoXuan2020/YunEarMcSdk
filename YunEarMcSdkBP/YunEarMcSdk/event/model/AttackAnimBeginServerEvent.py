# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AttackAnimBeginServerEvent(ServerEvent):

    def __init__(self, callback):
        super(AttackAnimBeginServerEvent, self).__init__(callback)
        self.id_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]

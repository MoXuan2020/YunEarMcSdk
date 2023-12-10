# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AttackAnimEndServerEvent(ServerEvent):

    def __init__(self, callback):
        super(AttackAnimEndServerEvent, self).__init__(callback)
        self.id = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")

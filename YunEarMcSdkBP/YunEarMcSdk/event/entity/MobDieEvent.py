# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class MobDieEvent(ServerEvent):

    def __init__(self, callback):
        super(MobDieEvent, self).__init__(callback)
        self.id = None
        self.attacker = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.attacker = args.get("attacker")

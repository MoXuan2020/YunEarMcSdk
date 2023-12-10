# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerDieEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerDieEvent, self).__init__(callback)
        self.id_ = None
        self.attacker_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
        self.attacker_ = args.get("attacker")

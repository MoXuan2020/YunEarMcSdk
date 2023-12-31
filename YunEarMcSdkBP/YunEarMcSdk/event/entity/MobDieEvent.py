# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class MobDieEvent(ServerEvent):

    def __init__(self, callback):
        super(MobDieEvent, self).__init__(callback)
        self.id_ = None
        self.attacker_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]
        self.attacker_ = args["attacker"]

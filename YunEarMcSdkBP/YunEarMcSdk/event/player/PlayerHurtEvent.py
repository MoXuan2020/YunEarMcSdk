# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerHurtEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerHurtEvent, self).__init__(callback)
        self.id_ = None
        self.attacker_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]
        self.attacker_ = args["attacker"]

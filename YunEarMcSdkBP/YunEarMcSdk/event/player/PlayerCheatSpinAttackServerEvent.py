# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerCheatSpinAttackServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerCheatSpinAttackServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.isStart_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.isStart_ = args["isStart"]

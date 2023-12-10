# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerCheatSpinAttackServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerCheatSpinAttackServerEvent, self).__init__(callback)
        self.playerId = None
        self.isStart = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.isStart = args.get("isStart")

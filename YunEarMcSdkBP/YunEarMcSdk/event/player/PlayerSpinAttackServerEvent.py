# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerSpinAttackServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerSpinAttackServerEvent, self).__init__(callback)
        self.playerId = None
        self.isInWaterOrRain = None
        self.isRiding = None
        self.isStart = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.isInWaterOrRain = args.get("isInWaterOrRain")
        self.isRiding = args.get("isRiding")
        self.isStart = args.get("isStart")

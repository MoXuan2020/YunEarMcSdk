# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerSpinAttackServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerSpinAttackServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.isInWaterOrRain_ = None
        self.isRiding_ = None
        self.isStart_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.isInWaterOrRain_ = args.get("isInWaterOrRain")
        self.isRiding_ = args.get("isRiding")
        self.isStart_ = args.get("isStart")

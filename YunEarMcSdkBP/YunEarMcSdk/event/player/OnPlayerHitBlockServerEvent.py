# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnPlayerHitBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnPlayerHitBlockServerEvent, self).__init__(callback)
        self.playerId = None
        self.posX = None
        self.posY = None
        self.posZ = None
        self.blockId = None
        self.auxValue = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.blockId = args.get("blockId")
        self.auxValue = args.get("auxValue")
        self.dimensionId = args.get("dimensionId")

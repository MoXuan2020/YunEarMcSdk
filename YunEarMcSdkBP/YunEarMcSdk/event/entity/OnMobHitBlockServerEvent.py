# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnMobHitBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnMobHitBlockServerEvent, self).__init__(callback)
        self.entityId = None
        self.posX = None
        self.posY = None
        self.posZ = None
        self.blockId = None
        self.auxValue = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.blockId = args.get("blockId")
        self.auxValue = args.get("auxValue")
        self.dimensionId = args.get("dimensionId")

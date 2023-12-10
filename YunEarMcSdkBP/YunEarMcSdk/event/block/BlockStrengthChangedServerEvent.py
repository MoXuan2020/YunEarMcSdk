# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockStrengthChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockStrengthChangedServerEvent, self).__init__(callback)
        self.posX = None
        self.posY = None
        self.posZ = None
        self.blockName = None
        self.auxValue = None
        self.newStrength = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.blockName = args.get("blockName")
        self.auxValue = args.get("auxValue")
        self.newStrength = args.get("newStrength")
        self.dimensionId = args.get("dimensionId")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnStandOnBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnStandOnBlockServerEvent, self).__init__(callback)
        self.entityId = None
        self.dimensionId = None
        self.posX = None
        self.posY = None
        self.posZ = None
        self.motionX = None
        self.motionY = None
        self.motionZ = None
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.blockName = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.dimensionId = args.get("dimensionId")
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.motionX = args.get("motionX")
        self.motionY = args.get("motionY")
        self.motionZ = args.get("motionZ")
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.blockName = args.get("blockName")
        self.cancel = args.get("cancel")

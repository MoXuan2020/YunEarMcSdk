# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnAfterFallOnBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnAfterFallOnBlockClientEvent, self).__init__(callback)
        self.entityId = None
        self.posX = None
        self.posY = None
        self.posZ = None
        self.motionX = None
        self.motionY = None
        self.motionZ = None
        self.blockName = None
        self.calculate = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.motionX = args.get("motionX")
        self.motionY = args.get("motionY")
        self.motionZ = args.get("motionZ")
        self.blockName = args.get("blockName")
        self.calculate = args.get("calculate")

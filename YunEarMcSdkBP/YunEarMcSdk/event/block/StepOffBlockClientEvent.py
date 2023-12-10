# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StepOffBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StepOffBlockClientEvent, self).__init__(callback)
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.entityId = None
        self.blockName = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.entityId = args.get("entityId")
        self.blockName = args.get("blockName")
        self.dimensionId = args.get("dimensionId")

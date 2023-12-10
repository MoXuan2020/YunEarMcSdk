# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class StepOffBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(StepOffBlockServerEvent, self).__init__(callback)
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

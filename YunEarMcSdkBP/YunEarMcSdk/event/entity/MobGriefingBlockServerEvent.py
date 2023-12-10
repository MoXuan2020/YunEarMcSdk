# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class MobGriefingBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(MobGriefingBlockServerEvent, self).__init__(callback)
        self.cancel = None
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.entityId = None
        self.blockName = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.cancel = args.get("cancel")
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.entityId = args.get("entityId")
        self.blockName = args.get("blockName")
        self.dimensionId = args.get("dimensionId")

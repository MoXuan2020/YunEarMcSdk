# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnBeforeFallOnBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnBeforeFallOnBlockServerEvent, self).__init__(callback)
        self.entityId = None
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.blockName = None
        self.fallDistance = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.blockName = args.get("blockName")
        self.fallDistance = args.get("fallDistance")
        self.cancel = args.get("cancel")

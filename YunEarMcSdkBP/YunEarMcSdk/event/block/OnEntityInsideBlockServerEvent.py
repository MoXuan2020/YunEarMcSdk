# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnEntityInsideBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnEntityInsideBlockServerEvent, self).__init__(callback)
        self.entityId = None
        self.slowdownMultiX = None
        self.slowdownMultiY = None
        self.slowdownMultiZ = None
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.blockName = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.slowdownMultiX = args.get("slowdownMultiX")
        self.slowdownMultiY = args.get("slowdownMultiY")
        self.slowdownMultiZ = args.get("slowdownMultiZ")
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.blockName = args.get("blockName")
        self.cancel = args.get("cancel")

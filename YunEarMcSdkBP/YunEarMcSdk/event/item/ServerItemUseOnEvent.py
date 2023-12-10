# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerItemUseOnEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerItemUseOnEvent, self).__init__(callback)
        self.entityId = None
        self.itemDict = None
        self.x = None
        self.y = None
        self.z = None
        self.blockName = None
        self.blockAuxValue = None
        self.face = None
        self.dimensionId = None
        self.clickX = None
        self.clickY = None
        self.clickZ = None
        self.ret = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.itemDict = args.get("itemDict")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.blockName = args.get("blockName")
        self.blockAuxValue = args.get("blockAuxValue")
        self.face = args.get("face")
        self.dimensionId = args.get("dimensionId")
        self.clickX = args.get("clickX")
        self.clickY = args.get("clickY")
        self.clickZ = args.get("clickZ")
        self.ret = args.get("ret")

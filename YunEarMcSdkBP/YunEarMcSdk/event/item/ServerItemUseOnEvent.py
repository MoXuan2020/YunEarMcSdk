# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerItemUseOnEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerItemUseOnEvent, self).__init__(callback)
        self.entityId_ = None
        self.itemDict_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.blockName_ = None
        self.blockAuxValue_ = None
        self.face_ = None
        self.dimensionId_ = None
        self.clickX_ = None
        self.clickY_ = None
        self.clickZ_ = None
        self.ret_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.itemDict_ = args.get("itemDict")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.blockName_ = args.get("blockName")
        self.blockAuxValue_ = args.get("blockAuxValue")
        self.face_ = args.get("face")
        self.dimensionId_ = args.get("dimensionId")
        self.clickX_ = args.get("clickX")
        self.clickY_ = args.get("clickY")
        self.clickZ_ = args.get("clickZ")
        self.ret_ = args.get("ret")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PistonActionServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PistonActionServerEvent, self).__init__(callback)
        self.cancel_ = None
        self.action_ = None
        self.pistonFacing_ = None
        self.pistonMoveFacing_ = None
        self.dimensionId_ = None
        self.pistonX_ = None
        self.pistonY_ = None
        self.pistonZ_ = None
        self.blockList_ = None
        self.breakBlockList_ = None
        self.entityList_ = None

    def CreateFromArgs(self, args):
        self.cancel_ = args.get("cancel")
        self.action_ = args.get("action")
        self.pistonFacing_ = args.get("pistonFacing")
        self.pistonMoveFacing_ = args.get("pistonMoveFacing")
        self.dimensionId_ = args.get("dimensionId")
        self.pistonX_ = args.get("pistonX")
        self.pistonY_ = args.get("pistonY")
        self.pistonZ_ = args.get("pistonZ")
        self.blockList_ = args.get("blockList")
        self.breakBlockList_ = args.get("breakBlockList")
        self.entityList_ = args.get("entityList")

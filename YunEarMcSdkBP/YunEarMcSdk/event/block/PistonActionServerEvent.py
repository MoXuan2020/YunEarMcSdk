# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PistonActionServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PistonActionServerEvent, self).__init__(callback)
        self.cancel = None
        self.action = None
        self.pistonFacing = None
        self.pistonMoveFacing = None
        self.dimensionId = None
        self.pistonX = None
        self.pistonY = None
        self.pistonZ = None
        self.blockList = None
        self.breakBlockList = None
        self.entityList = None

    def CreateFromArgs(self, args):
        self.cancel = args.get("cancel")
        self.action = args.get("action")
        self.pistonFacing = args.get("pistonFacing")
        self.pistonMoveFacing = args.get("pistonMoveFacing")
        self.dimensionId = args.get("dimensionId")
        self.pistonX = args.get("pistonX")
        self.pistonY = args.get("pistonY")
        self.pistonZ = args.get("pistonZ")
        self.blockList = args.get("blockList")
        self.breakBlockList = args.get("breakBlockList")
        self.entityList = args.get("entityList")

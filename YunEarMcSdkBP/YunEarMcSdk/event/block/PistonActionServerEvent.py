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
        self.cancel_ = args["cancel"]
        self.action_ = args["action"]
        self.pistonFacing_ = args["pistonFacing"]
        self.pistonMoveFacing_ = args["pistonMoveFacing"]
        self.dimensionId_ = args["dimensionId"]
        self.pistonX_ = args["pistonX"]
        self.pistonY_ = args["pistonY"]
        self.pistonZ_ = args["pistonZ"]
        self.blockList_ = args["blockList"]
        self.breakBlockList_ = args["breakBlockList"]
        self.entityList_ = args["entityList"]

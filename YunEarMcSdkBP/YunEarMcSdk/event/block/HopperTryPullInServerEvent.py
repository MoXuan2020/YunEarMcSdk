# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class HopperTryPullInServerEvent(ServerEvent):

    def __init__(self, callback):
        super(HopperTryPullInServerEvent, self).__init__(callback)
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.abovePosX_ = None
        self.abovePosY_ = None
        self.abovePosZ_ = None
        self.dimensionId_ = None
        self.canHopper_ = None

    def CreateFromArgs(self, args):
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.abovePosX_ = args["abovePosX"]
        self.abovePosY_ = args["abovePosY"]
        self.abovePosZ_ = args["abovePosZ"]
        self.dimensionId_ = args["dimensionId"]
        self.canHopper_ = args["canHopper"]

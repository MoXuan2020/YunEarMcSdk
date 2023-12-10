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
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.abovePosX_ = args.get("abovePosX")
        self.abovePosY_ = args.get("abovePosY")
        self.abovePosZ_ = args.get("abovePosZ")
        self.dimensionId_ = args.get("dimensionId")
        self.canHopper_ = args.get("canHopper")

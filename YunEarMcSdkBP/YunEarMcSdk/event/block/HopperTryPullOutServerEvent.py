# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class HopperTryPullOutServerEvent(ServerEvent):

    def __init__(self, callback):
        super(HopperTryPullOutServerEvent, self).__init__(callback)
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.attachedPosX_ = None
        self.attachedPosY_ = None
        self.attachedPosZ_ = None
        self.dimensionId_ = None
        self.canHopper_ = None

    def CreateFromArgs(self, args):
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.attachedPosX_ = args.get("attachedPosX")
        self.attachedPosY_ = args.get("attachedPosY")
        self.attachedPosZ_ = args.get("attachedPosZ")
        self.dimensionId_ = args.get("dimensionId")
        self.canHopper_ = args.get("canHopper")

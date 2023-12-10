# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class HopperTryPullOutServerEvent(ServerEvent):

    def __init__(self, callback):
        super(HopperTryPullOutServerEvent, self).__init__(callback)
        self.x = None
        self.y = None
        self.z = None
        self.attachedPosX = None
        self.attachedPosY = None
        self.attachedPosZ = None
        self.dimensionId = None
        self.canHopper = None

    def CreateFromArgs(self, args):
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.attachedPosX = args.get("attachedPosX")
        self.attachedPosY = args.get("attachedPosY")
        self.attachedPosZ = args.get("attachedPosZ")
        self.dimensionId = args.get("dimensionId")
        self.canHopper = args.get("canHopper")

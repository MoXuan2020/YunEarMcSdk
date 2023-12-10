# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class HopperTryPullInServerEvent(ServerEvent):

    def __init__(self, callback):
        super(HopperTryPullInServerEvent, self).__init__(callback)
        self.x = None
        self.y = None
        self.z = None
        self.abovePosX = None
        self.abovePosY = None
        self.abovePosZ = None
        self.dimensionId = None
        self.canHopper = None

    def CreateFromArgs(self, args):
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.abovePosX = args.get("abovePosX")
        self.abovePosY = args.get("abovePosY")
        self.abovePosZ = args.get("abovePosZ")
        self.dimensionId = args.get("dimensionId")
        self.canHopper = args.get("canHopper")

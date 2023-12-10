# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlaceNeteaseStructureFeatureEvent(ServerEvent):

    def __init__(self, callback):
        super(PlaceNeteaseStructureFeatureEvent, self).__init__(callback)
        self.structureName = None
        self.x = None
        self.y = None
        self.z = None
        self.biomeType = None
        self.biomeName = None
        self.dimensionId = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.structureName = args.get("structureName")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.biomeType = args.get("biomeType")
        self.biomeName = args.get("biomeName")
        self.dimensionId = args.get("dimensionId")
        self.cancel = args.get("cancel")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlaceNeteaseStructureFeatureEvent(ServerEvent):

    def __init__(self, callback):
        super(PlaceNeteaseStructureFeatureEvent, self).__init__(callback)
        self.structureName_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.biomeType_ = None
        self.biomeName_ = None
        self.dimensionId_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.structureName_ = args.get("structureName")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.biomeType_ = args.get("biomeType")
        self.biomeName_ = args.get("biomeName")
        self.dimensionId_ = args.get("dimensionId")
        self.cancel_ = args.get("cancel")

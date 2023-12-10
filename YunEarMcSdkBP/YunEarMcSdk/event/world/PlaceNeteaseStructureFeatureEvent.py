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
        self.structureName_ = args["structureName"]
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.biomeType_ = args["biomeType"]
        self.biomeName_ = args["biomeName"]
        self.dimensionId_ = args["dimensionId"]
        self.cancel_ = args["cancel"]

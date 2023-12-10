# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlaceNeteaseLargeFeatureServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlaceNeteaseLargeFeatureServerEvent, self).__init__(callback)
        self.dimensionId = None
        self.pos = None
        self.rot = None
        self.depth = None
        self.centerPool = None
        self.ignoreFitInContext = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.dimensionId = args.get("dimensionId")
        self.pos = args.get("pos")
        self.rot = args.get("rot")
        self.depth = args.get("depth")
        self.centerPool = args.get("centerPool")
        self.ignoreFitInContext = args.get("ignoreFitInContext")
        self.cancel = args.get("cancel")

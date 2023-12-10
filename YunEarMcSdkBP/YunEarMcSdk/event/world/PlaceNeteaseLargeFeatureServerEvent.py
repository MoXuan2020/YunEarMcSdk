# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlaceNeteaseLargeFeatureServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlaceNeteaseLargeFeatureServerEvent, self).__init__(callback)
        self.dimensionId_ = None
        self.pos_ = None
        self.rot_ = None
        self.depth_ = None
        self.centerPool_ = None
        self.ignoreFitInContext_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.dimensionId_ = args.get("dimensionId")
        self.pos_ = args.get("pos")
        self.rot_ = args.get("rot")
        self.depth_ = args.get("depth")
        self.centerPool_ = args.get("centerPool")
        self.ignoreFitInContext_ = args.get("ignoreFitInContext")
        self.cancel_ = args.get("cancel")

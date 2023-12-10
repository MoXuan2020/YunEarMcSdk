# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ExplosionServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ExplosionServerEvent, self).__init__(callback)
        self.blocks_ = None
        self.victims_ = None
        self.sourceId_ = None
        self.explodePos_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.blocks_ = args.get("blocks")
        self.victims_ = args.get("victims")
        self.sourceId_ = args.get("sourceId")
        self.explodePos_ = args.get("explodePos")
        self.dimensionId_ = args.get("dimensionId")

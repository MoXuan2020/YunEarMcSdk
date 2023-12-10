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
        self.blocks_ = args["blocks"]
        self.victims_ = args["victims"]
        self.sourceId_ = args["sourceId"]
        self.explodePos_ = args["explodePos"]
        self.dimensionId_ = args["dimensionId"]

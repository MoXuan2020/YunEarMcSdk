# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ExplosionServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ExplosionServerEvent, self).__init__(callback)
        self.blocks = None
        self.victims = None
        self.sourceId = None
        self.explodePos = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.blocks = args.get("blocks")
        self.victims = args.get("victims")
        self.sourceId = args.get("sourceId")
        self.explodePos = args.get("explodePos")
        self.dimensionId = args.get("dimensionId")

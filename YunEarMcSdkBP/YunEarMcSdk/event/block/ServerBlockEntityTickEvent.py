# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerBlockEntityTickEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerBlockEntityTickEvent, self).__init__(callback)
        self.blockName = None
        self.dimension = None
        self.posX = None
        self.posY = None
        self.posZ = None

    def CreateFromArgs(self, args):
        self.blockName = args.get("blockName")
        self.dimension = args.get("dimension")
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")

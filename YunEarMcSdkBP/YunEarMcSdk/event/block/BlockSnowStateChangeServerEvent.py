# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockSnowStateChangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockSnowStateChangeServerEvent, self).__init__(callback)
        self.dimension = None
        self.x = None
        self.y = None
        self.z = None
        self.turnSnow = None
        self.setBlockType = None

    def CreateFromArgs(self, args):
        self.dimension = args.get("dimension")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.turnSnow = args.get("turnSnow")
        self.setBlockType = args.get("setBlockType")

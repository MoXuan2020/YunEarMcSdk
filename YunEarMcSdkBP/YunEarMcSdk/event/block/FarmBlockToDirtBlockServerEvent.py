# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FarmBlockToDirtBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FarmBlockToDirtBlockServerEvent, self).__init__(callback)
        self.dimension = None
        self.x = None
        self.y = None
        self.z = None
        self.setBlockType = None

    def CreateFromArgs(self, args):
        self.dimension = args.get("dimension")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.setBlockType = args.get("setBlockType")

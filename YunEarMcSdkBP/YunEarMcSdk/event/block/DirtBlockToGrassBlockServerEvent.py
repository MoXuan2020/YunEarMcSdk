# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class DirtBlockToGrassBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(DirtBlockToGrassBlockServerEvent, self).__init__(callback)
        self.dimension = None
        self.x = None
        self.y = None
        self.z = None

    def CreateFromArgs(self, args):
        self.dimension = args.get("dimension")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")

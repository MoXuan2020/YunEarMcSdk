# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockRemoveServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockRemoveServerEvent, self).__init__(callback)
        self.x = None
        self.y = None
        self.z = None
        self.fullName = None
        self.auxValue = None
        self.dimension = None

    def CreateFromArgs(self, args):
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.fullName = args.get("fullName")
        self.auxValue = args.get("auxValue")
        self.dimension = args.get("dimension")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChunkGeneratedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChunkGeneratedServerEvent, self).__init__(callback)
        self.dimension = None
        self.blockEntityData = None

    def CreateFromArgs(self, args):
        self.dimension = args.get("dimension")
        self.blockEntityData = args.get("blockEntityData")

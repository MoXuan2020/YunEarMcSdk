# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChunkGeneratedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChunkGeneratedServerEvent, self).__init__(callback)
        self.dimension_ = None
        self.blockEntityData_ = None

    def CreateFromArgs(self, args):
        self.dimension_ = args.get("dimension")
        self.blockEntityData_ = args.get("blockEntityData")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChunkLoadedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChunkLoadedServerEvent, self).__init__(callback)
        self.dimension = None
        self.chunkPosX = None
        self.chunkPosZ = None
        self.blockEntities = None

    def CreateFromArgs(self, args):
        self.dimension = args.get("dimension")
        self.chunkPosX = args.get("chunkPosX")
        self.chunkPosZ = args.get("chunkPosZ")
        self.blockEntities = args.get("blockEntities")

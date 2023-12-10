# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChunkAcquireDiscardedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChunkAcquireDiscardedServerEvent, self).__init__(callback)
        self.dimension = None
        self.chunkPosX = None
        self.chunkPosZ = None
        self.entities = None
        self.blockEntities = None

    def CreateFromArgs(self, args):
        self.dimension = args.get("dimension")
        self.chunkPosX = args.get("chunkPosX")
        self.chunkPosZ = args.get("chunkPosZ")
        self.entities = args.get("entities")
        self.blockEntities = args.get("blockEntities")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChunkLoadedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChunkLoadedServerEvent, self).__init__(callback)
        self.dimension_ = None
        self.chunkPosX_ = None
        self.chunkPosZ_ = None
        self.blockEntities_ = None

    def CreateFromArgs(self, args):
        self.dimension_ = args.get("dimension")
        self.chunkPosX_ = args.get("chunkPosX")
        self.chunkPosZ_ = args.get("chunkPosZ")
        self.blockEntities_ = args.get("blockEntities")

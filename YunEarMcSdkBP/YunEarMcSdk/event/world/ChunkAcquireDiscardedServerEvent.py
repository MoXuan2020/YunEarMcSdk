# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChunkAcquireDiscardedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChunkAcquireDiscardedServerEvent, self).__init__(callback)
        self.dimension_ = None
        self.chunkPosX_ = None
        self.chunkPosZ_ = None
        self.entities_ = None
        self.blockEntities_ = None

    def CreateFromArgs(self, args):
        self.dimension_ = args["dimension"]
        self.chunkPosX_ = args["chunkPosX"]
        self.chunkPosZ_ = args["chunkPosZ"]
        self.entities_ = args["entities"]
        self.blockEntities_ = args["blockEntities"]

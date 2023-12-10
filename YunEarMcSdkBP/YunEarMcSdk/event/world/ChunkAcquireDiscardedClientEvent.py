# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ChunkAcquireDiscardedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ChunkAcquireDiscardedClientEvent, self).__init__(callback)
        self.dimension_ = None
        self.chunkPosX_ = None
        self.chunkPosZ_ = None

    def CreateFromArgs(self, args):
        self.dimension_ = args["dimension"]
        self.chunkPosX_ = args["chunkPosX"]
        self.chunkPosZ_ = args["chunkPosZ"]

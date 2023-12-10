# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ChunkAcquireDiscardedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ChunkAcquireDiscardedClientEvent, self).__init__(callback)
        self.dimension = None
        self.chunkPosX = None
        self.chunkPosZ = None

    def CreateFromArgs(self, args):
        self.dimension = args.get("dimension")
        self.chunkPosX = args.get("chunkPosX")
        self.chunkPosZ = args.get("chunkPosZ")

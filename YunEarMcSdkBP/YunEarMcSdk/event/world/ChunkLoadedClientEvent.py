# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ChunkLoadedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ChunkLoadedClientEvent, self).__init__(callback)
        self.dimension_ = None
        self.chunkPosX_ = None
        self.chunkPosZ_ = None

    def CreateFromArgs(self, args):
        self.dimension_ = args.get("dimension")
        self.chunkPosX_ = args.get("chunkPosX")
        self.chunkPosZ_ = args.get("chunkPosZ")

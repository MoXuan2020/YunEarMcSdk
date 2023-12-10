# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FarmBlockToDirtBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FarmBlockToDirtBlockServerEvent, self).__init__(callback)
        self.dimension_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.setBlockType_ = None

    def CreateFromArgs(self, args):
        self.dimension_ = args.get("dimension")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.setBlockType_ = args.get("setBlockType")

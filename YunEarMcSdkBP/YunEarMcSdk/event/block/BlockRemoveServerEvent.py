# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockRemoveServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockRemoveServerEvent, self).__init__(callback)
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.fullName_ = None
        self.auxValue_ = None
        self.dimension_ = None

    def CreateFromArgs(self, args):
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.fullName_ = args.get("fullName")
        self.auxValue_ = args.get("auxValue")
        self.dimension_ = args.get("dimension")

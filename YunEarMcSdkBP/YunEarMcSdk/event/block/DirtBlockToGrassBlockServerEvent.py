# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class DirtBlockToGrassBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(DirtBlockToGrassBlockServerEvent, self).__init__(callback)
        self.dimension_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None

    def CreateFromArgs(self, args):
        self.dimension_ = args.get("dimension")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")

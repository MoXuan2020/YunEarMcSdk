# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockLiquidStateChangeAfterServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockLiquidStateChangeAfterServerEvent, self).__init__(callback)
        self.blockName_ = None
        self.auxValue_ = None
        self.dimension_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.turnLiquid_ = None

    def CreateFromArgs(self, args):
        self.blockName_ = args["blockName"]
        self.auxValue_ = args["auxValue"]
        self.dimension_ = args["dimension"]
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.turnLiquid_ = args["turnLiquid"]

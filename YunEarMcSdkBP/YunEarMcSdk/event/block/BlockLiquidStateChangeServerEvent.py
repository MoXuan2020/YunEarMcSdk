# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockLiquidStateChangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockLiquidStateChangeServerEvent, self).__init__(callback)
        self.blockName_ = None
        self.auxValue_ = None
        self.dimension_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.turnLiquid_ = None

    def CreateFromArgs(self, args):
        self.blockName_ = args.get("blockName")
        self.auxValue_ = args.get("auxValue")
        self.dimension_ = args.get("dimension")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.turnLiquid_ = args.get("turnLiquid")

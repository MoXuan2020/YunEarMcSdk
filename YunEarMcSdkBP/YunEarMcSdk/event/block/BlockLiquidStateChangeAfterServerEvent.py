# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockLiquidStateChangeAfterServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockLiquidStateChangeAfterServerEvent, self).__init__(callback)
        self.blockName = None
        self.auxValue = None
        self.dimension = None
        self.x = None
        self.y = None
        self.z = None
        self.turnLiquid = None

    def CreateFromArgs(self, args):
        self.blockName = args.get("blockName")
        self.auxValue = args.get("auxValue")
        self.dimension = args.get("dimension")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.turnLiquid = args.get("turnLiquid")

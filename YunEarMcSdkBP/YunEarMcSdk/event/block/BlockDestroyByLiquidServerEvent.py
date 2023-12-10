# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockDestroyByLiquidServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockDestroyByLiquidServerEvent, self).__init__(callback)
        self.x = None
        self.y = None
        self.z = None
        self.liquidName = None
        self.blockName = None
        self.auxValue = None

    def CreateFromArgs(self, args):
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.liquidName = args.get("liquidName")
        self.blockName = args.get("blockName")
        self.auxValue = args.get("auxValue")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockDestroyByLiquidServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockDestroyByLiquidServerEvent, self).__init__(callback)
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.liquidName_ = None
        self.blockName_ = None
        self.auxValue_ = None

    def CreateFromArgs(self, args):
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.liquidName_ = args.get("liquidName")
        self.blockName_ = args.get("blockName")
        self.auxValue_ = args.get("auxValue")

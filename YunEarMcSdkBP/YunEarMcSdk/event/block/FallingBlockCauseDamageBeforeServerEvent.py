# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FallingBlockCauseDamageBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FallingBlockCauseDamageBeforeServerEvent, self).__init__(callback)
        self.fallingBlockId_ = None
        self.fallingBlockX_ = None
        self.fallingBlockY_ = None
        self.fallingBlockZ_ = None
        self.blockName_ = None
        self.dimensionId_ = None
        self.collidingEntitys_ = None
        self.fallTickAmount_ = None
        self.fallDistance_ = None
        self.isHarmful_ = None
        self.fallDamage_ = None

    def CreateFromArgs(self, args):
        self.fallingBlockId_ = args["fallingBlockId"]
        self.fallingBlockX_ = args["fallingBlockX"]
        self.fallingBlockY_ = args["fallingBlockY"]
        self.fallingBlockZ_ = args["fallingBlockZ"]
        self.blockName_ = args["blockName"]
        self.dimensionId_ = args["dimensionId"]
        self.collidingEntitys_ = args["collidingEntitys"]
        self.fallTickAmount_ = args["fallTickAmount"]
        self.fallDistance_ = args["fallDistance"]
        self.isHarmful_ = args["isHarmful"]
        self.fallDamage_ = args["fallDamage"]

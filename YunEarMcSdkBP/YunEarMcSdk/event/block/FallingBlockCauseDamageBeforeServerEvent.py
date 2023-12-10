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
        self.fallingBlockId_ = args.get("fallingBlockId")
        self.fallingBlockX_ = args.get("fallingBlockX")
        self.fallingBlockY_ = args.get("fallingBlockY")
        self.fallingBlockZ_ = args.get("fallingBlockZ")
        self.blockName_ = args.get("blockName")
        self.dimensionId_ = args.get("dimensionId")
        self.collidingEntitys_ = args.get("collidingEntitys")
        self.fallTickAmount_ = args.get("fallTickAmount")
        self.fallDistance_ = args.get("fallDistance")
        self.isHarmful_ = args.get("isHarmful")
        self.fallDamage_ = args.get("fallDamage")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FallingBlockCauseDamageBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FallingBlockCauseDamageBeforeServerEvent, self).__init__(callback)
        self.fallingBlockId = None
        self.fallingBlockX = None
        self.fallingBlockY = None
        self.fallingBlockZ = None
        self.blockName = None
        self.dimensionId = None
        self.collidingEntitys = None
        self.fallTickAmount = None
        self.fallDistance = None
        self.isHarmful = None
        self.fallDamage = None

    def CreateFromArgs(self, args):
        self.fallingBlockId = args.get("fallingBlockId")
        self.fallingBlockX = args.get("fallingBlockX")
        self.fallingBlockY = args.get("fallingBlockY")
        self.fallingBlockZ = args.get("fallingBlockZ")
        self.blockName = args.get("blockName")
        self.dimensionId = args.get("dimensionId")
        self.collidingEntitys = args.get("collidingEntitys")
        self.fallTickAmount = args.get("fallTickAmount")
        self.fallDistance = args.get("fallDistance")
        self.isHarmful = args.get("isHarmful")
        self.fallDamage = args.get("fallDamage")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ProjectileDoHitEffectEvent(ServerEvent):

    def __init__(self, callback):
        super(ProjectileDoHitEffectEvent, self).__init__(callback)
        self.id = None
        self.hitTargetType = None
        self.targetId = None
        self.hitFace = None
        self.x = None
        self.y = None
        self.z = None
        self.blockPosX = None
        self.blockPosY = None
        self.blockPosZ = None
        self.srcId = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.hitTargetType = args.get("hitTargetType")
        self.targetId = args.get("targetId")
        self.hitFace = args.get("hitFace")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.blockPosX = args.get("blockPosX")
        self.blockPosY = args.get("blockPosY")
        self.blockPosZ = args.get("blockPosZ")
        self.srcId = args.get("srcId")
        self.cancel = args.get("cancel")

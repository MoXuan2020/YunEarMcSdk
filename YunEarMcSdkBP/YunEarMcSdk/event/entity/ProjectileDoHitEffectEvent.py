# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ProjectileDoHitEffectEvent(ServerEvent):

    def __init__(self, callback):
        super(ProjectileDoHitEffectEvent, self).__init__(callback)
        self.id_ = None
        self.hitTargetType_ = None
        self.targetId_ = None
        self.hitFace_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.blockPosX_ = None
        self.blockPosY_ = None
        self.blockPosZ_ = None
        self.srcId_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
        self.hitTargetType_ = args.get("hitTargetType")
        self.targetId_ = args.get("targetId")
        self.hitFace_ = args.get("hitFace")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.blockPosX_ = args.get("blockPosX")
        self.blockPosY_ = args.get("blockPosY")
        self.blockPosZ_ = args.get("blockPosZ")
        self.srcId_ = args.get("srcId")
        self.cancel_ = args.get("cancel")

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
        self.id_ = args["id"]
        self.hitTargetType_ = args["hitTargetType"]
        self.targetId_ = args["targetId"]
        self.hitFace_ = args["hitFace"]
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.blockPosX_ = args["blockPosX"]
        self.blockPosY_ = args["blockPosY"]
        self.blockPosZ_ = args["blockPosZ"]
        self.srcId_ = args["srcId"]
        self.cancel_ = args["cancel"]

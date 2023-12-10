# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnBeforeFallOnBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnBeforeFallOnBlockServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.blockName_ = None
        self.fallDistance_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.blockName_ = args.get("blockName")
        self.fallDistance_ = args.get("fallDistance")
        self.cancel_ = args.get("cancel")

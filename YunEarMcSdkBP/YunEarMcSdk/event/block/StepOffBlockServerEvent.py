# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class StepOffBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(StepOffBlockServerEvent, self).__init__(callback)
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.entityId_ = None
        self.blockName_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.entityId_ = args.get("entityId")
        self.blockName_ = args.get("blockName")
        self.dimensionId_ = args.get("dimensionId")

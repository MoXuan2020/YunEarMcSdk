# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StepOnBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StepOnBlockClientEvent, self).__init__(callback)
        self.cancel_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.entityId_ = None
        self.blockName_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.cancel_ = args.get("cancel")
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.entityId_ = args.get("entityId")
        self.blockName_ = args.get("blockName")
        self.dimensionId_ = args.get("dimensionId")

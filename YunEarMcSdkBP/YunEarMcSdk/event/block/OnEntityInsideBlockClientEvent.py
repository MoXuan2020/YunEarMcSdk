# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnEntityInsideBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnEntityInsideBlockClientEvent, self).__init__(callback)
        self.entityId_ = None
        self.dimensionId_ = None
        self.slowdownMultiX_ = None
        self.slowdownMultiY_ = None
        self.slowdownMultiZ_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.blockName_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.dimensionId_ = args.get("dimensionId")
        self.slowdownMultiX_ = args.get("slowdownMultiX")
        self.slowdownMultiY_ = args.get("slowdownMultiY")
        self.slowdownMultiZ_ = args.get("slowdownMultiZ")
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.blockName_ = args.get("blockName")
        self.cancel_ = args.get("cancel")

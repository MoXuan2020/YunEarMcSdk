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
        self.entityId_ = args["entityId"]
        self.dimensionId_ = args["dimensionId"]
        self.slowdownMultiX_ = args["slowdownMultiX"]
        self.slowdownMultiY_ = args["slowdownMultiY"]
        self.slowdownMultiZ_ = args["slowdownMultiZ"]
        self.blockX_ = args["blockX"]
        self.blockY_ = args["blockY"]
        self.blockZ_ = args["blockZ"]
        self.blockName_ = args["blockName"]
        self.cancel_ = args["cancel"]

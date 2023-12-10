# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnContainerFillLoottableServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnContainerFillLoottableServerEvent, self).__init__(callback)
        self.loottable_ = None
        self.playerId_ = None
        self.itemList_ = None
        self.dirty_ = None

    def CreateFromArgs(self, args):
        self.loottable_ = args["loottable"]
        self.playerId_ = args["playerId"]
        self.itemList_ = args["itemList"]
        self.dirty_ = args["dirty"]

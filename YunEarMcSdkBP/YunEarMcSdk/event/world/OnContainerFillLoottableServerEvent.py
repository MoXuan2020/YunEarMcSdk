# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnContainerFillLoottableServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnContainerFillLoottableServerEvent, self).__init__(callback)
        self.loottable = None
        self.playerId = None
        self.itemList = None
        self.dirty = None

    def CreateFromArgs(self, args):
        self.loottable = args.get("loottable")
        self.playerId = args.get("playerId")
        self.itemList = args.get("itemList")
        self.dirty = args.get("dirty")

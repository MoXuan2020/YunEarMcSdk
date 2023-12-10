# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnCarriedNewItemChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnCarriedNewItemChangedServerEvent, self).__init__(callback)
        self.oldItemDict_ = None
        self.newItemDict_ = None
        self.playerId_ = None

    def CreateFromArgs(self, args):
        self.oldItemDict_ = args["oldItemDict"]
        self.newItemDict_ = args["newItemDict"]
        self.playerId_ = args["playerId"]

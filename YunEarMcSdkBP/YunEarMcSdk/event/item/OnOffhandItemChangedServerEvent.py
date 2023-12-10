# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnOffhandItemChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnOffhandItemChangedServerEvent, self).__init__(callback)
        self.oldItemDict_ = None
        self.newItemDict_ = None
        self.playerId_ = None

    def CreateFromArgs(self, args):
        self.oldItemDict_ = args.get("oldItemDict")
        self.newItemDict_ = args.get("newItemDict")
        self.playerId_ = args.get("playerId")

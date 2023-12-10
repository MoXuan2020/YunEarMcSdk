# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerFeedEntityServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerFeedEntityServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.entityId_ = None
        self.itemDict_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.entityId_ = args.get("entityId")
        self.itemDict_ = args.get("itemDict")
        self.cancel_ = args.get("cancel")

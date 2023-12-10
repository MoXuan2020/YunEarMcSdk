# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnPlayerBlockedByShieldBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnPlayerBlockedByShieldBeforeServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.sourceId_ = None
        self.itemDict_ = None
        self.damage_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.sourceId_ = args.get("sourceId")
        self.itemDict_ = args.get("itemDict")
        self.damage_ = args.get("damage")

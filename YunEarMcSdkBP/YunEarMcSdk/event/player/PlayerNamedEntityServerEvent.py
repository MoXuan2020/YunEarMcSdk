# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerNamedEntityServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerNamedEntityServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.entityId_ = None
        self.preName_ = None
        self.afterName_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.entityId_ = args.get("entityId")
        self.preName_ = args.get("preName")
        self.afterName_ = args.get("afterName")
        self.cancel_ = args.get("cancel")

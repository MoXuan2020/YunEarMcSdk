# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerNamedEntityServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerNamedEntityServerEvent, self).__init__(callback)
        self.playerId = None
        self.entityId = None
        self.preName = None
        self.afterName = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.entityId = args.get("entityId")
        self.preName = args.get("preName")
        self.afterName = args.get("afterName")
        self.cancel = args.get("cancel")

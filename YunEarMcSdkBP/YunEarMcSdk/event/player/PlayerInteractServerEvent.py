# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerInteractServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerInteractServerEvent, self).__init__(callback)
        self.cancel = None
        self.playerId = None
        self.itemDict = None
        self.victimId = None

    def CreateFromArgs(self, args):
        self.cancel = args.get("cancel")
        self.playerId = args.get("playerId")
        self.itemDict = args.get("itemDict")
        self.victimId = args.get("victimId")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerInteractServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerInteractServerEvent, self).__init__(callback)
        self.cancel_ = None
        self.playerId_ = None
        self.itemDict_ = None
        self.victimId_ = None

    def CreateFromArgs(self, args):
        self.cancel_ = args.get("cancel")
        self.playerId_ = args.get("playerId")
        self.itemDict_ = args.get("itemDict")
        self.victimId_ = args.get("victimId")

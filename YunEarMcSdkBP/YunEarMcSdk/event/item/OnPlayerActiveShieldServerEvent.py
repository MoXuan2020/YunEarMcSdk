# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnPlayerActiveShieldServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnPlayerActiveShieldServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.isActive_ = None
        self.itemDict_ = None
        self.cancelable_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.isActive_ = args.get("isActive")
        self.itemDict_ = args.get("itemDict")
        self.cancelable_ = args.get("cancelable")
        self.cancel_ = args.get("cancel")

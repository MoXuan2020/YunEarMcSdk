# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AddServerPlayerEvent(ServerEvent):

    def __init__(self, callback):
        super(AddServerPlayerEvent, self).__init__(callback)
        self.id = None
        self.isTransfer = None
        self.isReconnect = None
        self.isPeUser = None
        self.transferParam = None
        self.uid = None
        self.proxyId = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.isTransfer = args.get("isTransfer")
        self.isReconnect = args.get("isReconnect")
        self.isPeUser = args.get("isPeUser")
        self.transferParam = args.get("transferParam")
        self.uid = args.get("uid")
        self.proxyId = args.get("proxyId")

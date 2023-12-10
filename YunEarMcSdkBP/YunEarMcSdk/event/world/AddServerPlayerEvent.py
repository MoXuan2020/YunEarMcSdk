# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AddServerPlayerEvent(ServerEvent):

    def __init__(self, callback):
        super(AddServerPlayerEvent, self).__init__(callback)
        self.id_ = None
        self.isTransfer_ = None
        self.isReconnect_ = None
        self.isPeUser_ = None
        self.transferParam_ = None
        self.uid_ = None
        self.proxyId_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
        self.isTransfer_ = args.get("isTransfer")
        self.isReconnect_ = args.get("isReconnect")
        self.isPeUser_ = args.get("isPeUser")
        self.transferParam_ = args.get("transferParam")
        self.uid_ = args.get("uid")
        self.proxyId_ = args.get("proxyId")

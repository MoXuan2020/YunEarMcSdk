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
        self.id_ = args["id"]
        self.isTransfer_ = args["isTransfer"]
        self.isReconnect_ = args["isReconnect"]
        self.isPeUser_ = args["isPeUser"]
        self.transferParam_ = args["transferParam"]
        self.uid_ = args["uid"]
        self.proxyId_ = args["proxyId"]

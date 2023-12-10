# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ActorAcquiredItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ActorAcquiredItemClientEvent, self).__init__(callback)
        self.actor_ = None
        self.secondaryActor_ = None
        self.itemDict_ = None
        self.acquireMethod_ = None

    def CreateFromArgs(self, args):
        self.actor_ = args.get("actor")
        self.secondaryActor_ = args.get("secondaryActor")
        self.itemDict_ = args.get("itemDict")
        self.acquireMethod_ = args.get("acquireMethod")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ActorAcquiredItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ActorAcquiredItemClientEvent, self).__init__(callback)
        self.actor = None
        self.secondaryActor = None
        self.itemDict = None
        self.acquireMethod = None

    def CreateFromArgs(self, args):
        self.actor = args.get("actor")
        self.secondaryActor = args.get("secondaryActor")
        self.itemDict = args.get("itemDict")
        self.acquireMethod = args.get("acquireMethod")

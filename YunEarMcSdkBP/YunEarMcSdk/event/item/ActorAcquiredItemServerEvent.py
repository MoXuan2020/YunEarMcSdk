# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ActorAcquiredItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ActorAcquiredItemServerEvent, self).__init__(callback)
        self.actor = None
        self.secondaryActor = None
        self.itemDict = None
        self.acquireMethod = None

    def CreateFromArgs(self, args):
        self.actor = args.get("actor")
        self.secondaryActor = args.get("secondaryActor")
        self.itemDict = args.get("itemDict")
        self.acquireMethod = args.get("acquireMethod")

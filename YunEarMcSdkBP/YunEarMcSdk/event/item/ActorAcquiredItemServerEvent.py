# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ActorAcquiredItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ActorAcquiredItemServerEvent, self).__init__(callback)
        self.actor_ = None
        self.secondaryActor_ = None
        self.itemDict_ = None
        self.acquireMethod_ = None

    def CreateFromArgs(self, args):
        self.actor_ = args["actor"]
        self.secondaryActor_ = args["secondaryActor"]
        self.itemDict_ = args["itemDict"]
        self.acquireMethod_ = args["acquireMethod"]

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityPickupItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityPickupItemServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.itemDict_ = None
        self.secondaryActor_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.itemDict_ = args["itemDict"]
        self.secondaryActor_ = args["secondaryActor"]

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class EntityModelChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(EntityModelChangedClientEvent, self).__init__(callback)
        self.entityId_ = None
        self.newModel_ = None
        self.oldModel_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.newModel_ = args["newModel"]
        self.oldModel_ = args["oldModel"]

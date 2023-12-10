# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityStartRidingEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityStartRidingEvent, self).__init__(callback)
        self.id = None
        self.rideId = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.rideId = args.get("rideId")

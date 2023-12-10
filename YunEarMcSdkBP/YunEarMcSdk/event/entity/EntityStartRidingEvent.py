# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityStartRidingEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityStartRidingEvent, self).__init__(callback)
        self.id_ = None
        self.rideId_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
        self.rideId_ = args.get("rideId")

# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityStopRidingEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityStopRidingEvent, self).__init__(callback)
        self.id = None
        self.rideId = None
        self.exitFromRider = None
        self.entityIsBeingDestroyed = None
        self.switchingRides = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.rideId = args.get("rideId")
        self.exitFromRider = args.get("exitFromRider")
        self.entityIsBeingDestroyed = args.get("entityIsBeingDestroyed")
        self.switchingRides = args.get("switchingRides")
        self.cancel = args.get("cancel")

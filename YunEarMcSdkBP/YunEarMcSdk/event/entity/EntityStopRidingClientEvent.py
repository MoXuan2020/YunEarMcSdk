# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class EntityStopRidingEvent(ClientEvent):

    def __init__(self, callback):
        super(EntityStopRidingEvent, self).__init__(callback)
        self.id_ = None
        self.rideId_ = None
        self.exitFromRider_ = None
        self.entityIsBeingDestroyed_ = None
        self.switchingRides_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
        self.rideId_ = args.get("rideId")
        self.exitFromRider_ = args.get("exitFromRider")
        self.entityIsBeingDestroyed_ = args.get("entityIsBeingDestroyed")
        self.switchingRides_ = args.get("switchingRides")
        self.cancel_ = args.get("cancel")

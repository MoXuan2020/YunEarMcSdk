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
        self.id_ = args["id"]
        self.rideId_ = args["rideId"]
        self.exitFromRider_ = args["exitFromRider"]
        self.entityIsBeingDestroyed_ = args["entityIsBeingDestroyed"]
        self.switchingRides_ = args["switchingRides"]
        self.cancel_ = args["cancel"]

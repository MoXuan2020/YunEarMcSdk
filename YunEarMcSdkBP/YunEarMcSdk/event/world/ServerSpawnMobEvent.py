# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerSpawnMobEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerSpawnMobEvent, self).__init__(callback)
        self.entityId_ = None
        self.identifier_ = None
        self.type_ = None
        self.baby_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.dimensionId_ = None
        self.realIdentifier_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.identifier_ = args["identifier"]
        self.type_ = args["type"]
        self.baby_ = args["baby"]
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.dimensionId_ = args["dimensionId"]
        self.realIdentifier_ = args["realIdentifier"]
        self.cancel_ = args["cancel"]

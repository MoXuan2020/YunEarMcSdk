# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityPlaceBlockAfterServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityPlaceBlockAfterServerEvent, self).__init__(callback)
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.fullName_ = None
        self.auxData_ = None
        self.entityId_ = None
        self.dimensionId_ = None
        self.face_ = None

    def CreateFromArgs(self, args):
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.fullName_ = args["fullName"]
        self.auxData_ = args["auxData"]
        self.entityId_ = args["entityId"]
        self.dimensionId_ = args["dimensionId"]
        self.face_ = args["face"]

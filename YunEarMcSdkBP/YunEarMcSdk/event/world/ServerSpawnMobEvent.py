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
        self.entityId_ = args.get("entityId")
        self.identifier_ = args.get("identifier")
        self.type_ = args.get("type")
        self.baby_ = args.get("baby")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.dimensionId_ = args.get("dimensionId")
        self.realIdentifier_ = args.get("realIdentifier")
        self.cancel_ = args.get("cancel")

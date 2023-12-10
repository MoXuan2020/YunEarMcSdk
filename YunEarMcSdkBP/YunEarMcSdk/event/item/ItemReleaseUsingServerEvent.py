# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ItemReleaseUsingServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ItemReleaseUsingServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.durationLeft_ = None
        self.itemDict_ = None
        self.maxUseDuration_ = None
        self.cancel_ = None
        self.changeItem_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.durationLeft_ = args["durationLeft"]
        self.itemDict_ = args["itemDict"]
        self.maxUseDuration_ = args["maxUseDuration"]
        self.cancel_ = args["cancel"]
        self.changeItem_ = args["changeItem"]

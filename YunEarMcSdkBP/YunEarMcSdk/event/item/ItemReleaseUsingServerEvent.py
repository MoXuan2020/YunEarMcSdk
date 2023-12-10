# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ItemReleaseUsingServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ItemReleaseUsingServerEvent, self).__init__(callback)
        self.playerId = None
        self.durationLeft = None
        self.itemDict = None
        self.maxUseDuration = None
        self.cancel = None
        self.changeItem = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.durationLeft = args.get("durationLeft")
        self.itemDict = args.get("itemDict")
        self.maxUseDuration = args.get("maxUseDuration")
        self.cancel = args.get("cancel")
        self.changeItem = args.get("changeItem")

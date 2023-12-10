# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ItemReleaseUsingClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ItemReleaseUsingClientEvent, self).__init__(callback)
        self.playerId = None
        self.durationLeft = None
        self.itemDict = None
        self.maxUseDuration = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.durationLeft = args.get("durationLeft")
        self.itemDict = args.get("itemDict")
        self.maxUseDuration = args.get("maxUseDuration")
        self.cancel = args.get("cancel")

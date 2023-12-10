# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnItemSlotButtonClickedEvent(ClientEvent):

    def __init__(self, callback):
        super(OnItemSlotButtonClickedEvent, self).__init__(callback)
        self.slotIndex_ = None

    def CreateFromArgs(self, args):
        self.slotIndex_ = args["slotIndex"]

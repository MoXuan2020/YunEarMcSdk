# -*- coding: utf-8 -*-


class Event(object):

    def __init__(self, callback):
        self.callback = callback
        self.sdk = None

    def CreateFromArgs(self, args):
        pass

    def BindSdk(self, sdk):
        self.sdk = sdk

    def __call__(self, args):
        self.CreateFromArgs(args)
        self.callback(self.sdk.mod, self)

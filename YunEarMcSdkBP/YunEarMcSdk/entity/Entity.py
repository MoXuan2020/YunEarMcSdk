# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

from YunEarMcSdk.event.ClientEvent import ClientEvent
from YunEarMcSdk.event.ServerEvent import ServerEvent


class Entity(object):

    def __init__(self, event, id):
        self.event = event
        self.id = id

    def GetApi(self):
        if isinstance(self.event, ServerEvent):
            return serverApi
        if isinstance(self.event, ClientEvent):
            return clientApi

    def GetEngineCompFactory(self):
        return self.GetApi().GetEngineCompFactory()

    def CreateEngineType(self):
        return self.GetEngineCompFactory().CreateEngineType(self.id)

    def GetEngineType(self):
        return self.CreateEngineType().GetEngineType()

    def GetEngineTypeStr(self):
        return self.CreateEngineType().GetEngineTypeStr()

    def CreateEntityDefinitions(self):
        return self.GetEngineCompFactory().CreateEntityDefinitions(self.id)

    def GetEntityDefinitions(self):
        return self.CreateEntityDefinitions().GetEntityDefinitions()

    def CreateAuxValue(self):
        return self.GetEngineCompFactory().CreateAuxValue(self.id)

    def GetAuxValue(self):
        return self.CreateAuxValue().GetAuxValue()

    def CreateDimension(self):
        return self.GetEngineCompFactory().CreateDimension(self.id)

    def ChangeEntityDimension(self, dimensionId, pos=None):
        return self.CreateDimension().ChangeEntityDimension(dimensionId, pos)

    def CreateEntityComponent(self):
        return self.GetEngineCompFactory().CreateEntityComponent(self.id)

    def GetAllComponentsName(self):
        return self.CreateEntityComponent().GetAllComponentsName()

    def CreateAttr(self):
        return self.GetEngineCompFactory().CreateAttr(self.id)

    def GetAttrMaxValue(self, type):
        return self.CreateAttr().GetAttrMaxValue(type)

    def GetAttrValue(self, attrType):
        return self.CreateAttr().GetAttrValue(attrType)

    def CreateRot(self):
        return self.GetEngineCompFactory().CreateRot(self.id)

    def GetBodyRot(self):
        return self.CreateRot().GetBodyRot()

    def CreateBreath(self):
        return self.GetEngineCompFactory().CreateBreath(self.id)

    def GetLevelId(self):
        return self.GetApi().GetLevelId()

    def CreateGame(self):
        return self.GetEngineCompFactory().CreateGame(self.GetLevelId())

    def GetCurrentAirSupply(self):
        if isinstance(self.event, ServerEvent):
            return self.CreateBreath().GetCurrentAirSupply()
        if isinstance(self.event, ClientEvent):
            return self.CreateGame().GetCurrentAirSupply(self.id)

    def GetDeathTime(self):
        return self.CreateEntityDefinitions().GetDeathTime()

    def GetEntityDimensionId(self):
        return self.CreateDimension().GetEntityDimensionId()

    def GetEntityFallDistance(self):
        return self.CreateEntityDefinitions().GetEntityFallDistance()

    def GetEntityLinksTag(self):
        return self.CreateEntityDefinitions().GetEntityLinksTag()

    def CreateActorOwner(self):
        return self.GetEngineCompFactory().CreateActorOwner(self.id)

    def GetEntityOwner(self):
        return self.CreateActorOwner().GetEntityOwner()

    def CreatePos(self):
        return self.GetEngineCompFactory().CreatePos(self.id)

    def GetFootPos(self):
        return self.CreatePos().GetFootPos()

    def CreateGravity(self):
        return self.GetEngineCompFactory().CreateGravity(self.id)

    def GetGravity(self):
        return self.CreateGravity().GetGravity()

    def GetLoadActors(self):
        return self.CreateGame().GetLoadActors()

    def GetMarkVariant(self):
        return self.CreateEntityDefinitions().GetMarkVariant()

    def GetMaxAirSupply(self):
        if isinstance(self.event, ServerEvent):
            return self.CreateBreath().GetMaxAirSupply()
        if isinstance(self.event, ClientEvent):
            return self.CreateGame().GetMaxAirSupply(self.id)

    def GetMobColor(self):
        return self.CreateEntityDefinitions().GetMobColor()

    def GetMobStrength(self):
        return self.CreateEntityDefinitions().GetMobStrength()

    def GetMobStrengthMax(self):
        return self.CreateEntityDefinitions().GetMobStrengthMax()

    def CreateName(self):
        return self.GetEngineCompFactory().CreateName(self.id)

    def GetName(self):
        return self.CreateName().GetName()

    def GetPos(self):
        return self.CreatePos().GetPos()

    def GetRiderId(self):
        return self.CreateGame().GetRiderId(self.id)

    def GetRot(self):
        return self.CreateRot().GetRot()

    def CreateCollisionBox(self):
        return self.GetEngineCompFactory().CreateCollisionBox(self.id)

    def GetSize(self):
        return self.CreateCollisionBox().GetSize()

    def GetTradeLevel(self):
        return self.CreateEntityDefinitions().GetTradeLevel()

    def GetTypeFamily(self):
        return self.CreateAttr().GetTypeFamily()

    def GetUnitBubbleAirSupply(self):
        return self.CreateBreath().GetUnitBubbleAirSupply()

    def GetVariant(self):
        return self.CreateEntityDefinitions().GetVariant()

    def HasChest(self):
        return self.CreateEntityDefinitions().HasChest()

    def HasComponent(self, attrType):
        return self.CreateEntityComponent().HasComponent(attrType)

    def HasShddled(self):
        return self.CreateEntityDefinitions().HasShddled()

    def IsAngry(self):
        return self.CreateEntityDefinitions().IsAngry()

    def IsBaby(self):
        return self.CreateEntityDefinitions().IsBaby()

    def IsConsumingAirSupply(self):
        return self.CreateBreath().IsConsumingAirSupply()

    def IsIllagerCaptain(self):
        return self.CreateEntityDefinitions().IsIllagerCaptain()

    def IsNaturallySpawned(self):
        return self.CreateEntityDefinitions().IsNaturallySpawned()

    def IsOutOfControl(self):
        return self.CreateEntityDefinitions().IsOutOfControl()

    def IsPregnant(self):
        return self.CreateEntityDefinitions().IsPregnant()

    def IsSheared(self):
        return self.CreateEntityDefinitions().IsSheared()

    def IsSitting(self):
        return self.CreateEntityDefinitions().IsSitting()

    def IsTamed(self):
        return self.CreateEntityDefinitions().IsTamed()

    def LockLocalPlayerRot(self, lock):
        return self.CreateRot().LockLocalPlayerRot(lock)

    def PromoteToIllagerCaptain(self):
        return self.CreateEntityDefinitions().PromoteToIllagerCaptain()

    def SetAngry(self, isAngry, targerId=""):
        return self.CreateEntityDefinitions().SetAngry(isAngry, targerId)

    def SetAsAdult(self):
        return self.CreateEntityDefinitions().SetAsAdult()

    def SetAttrMaxValue(self, type, value):
        return self.CreateAttr().SetAttrMaxValue(type, value)

    def SetAttrValue(self, attrType, value):
        return self.CreateAttr().SetAttrValue(attrType, value)

    def SetChest(self, hasChest):
        return self.CreateEntityDefinitions().SetChest(hasChest)

    def SetCurrentAirSupply(self, data):
        return self.CreateBreath().SetCurrentAirSupply(data)

    def SetEntityLookAtPos(self, targetPos, minTime, maxTime, reject):
        return self.CreateRot().SetEntityLookAtPos(targetPos, minTime, maxTime, reject)

    def SetEntityOwner(self, targetId):
        return self.CreateActorOwner().SetEntityOwner(targetId)

    def SetFootPos(self, footPos):
        return self.CreatePos().SetFootPos(footPos)

    def SetGravity(self, gravity):
        return self.CreateGravity().SetGravity(gravity)

    def SetMarkVariant(self, variantType):
        return self.CreateEntityDefinitions().SetMarkVariant(variantType)

    def SetMaxAirSupply(self, data):
        return self.CreateBreath().SetMaxAirSupply(data)

    def SetMobColor(self, colorType):
        return self.CreateEntityDefinitions().SetMobColor(colorType)

    def SetMobStrength(self, strength):
        return self.CreateEntityDefinitions().SetMobStrength(strength)

    def SetMobStrengthMax(self, strength):
        return self.CreateEntityDefinitions().SetMobStrengthMax(strength)

    def SetName(self, name):
        return self.CreateName().SetName(name)

    def SetOutOfControl(self, isOutOfControl):
        return self.CreateEntityDefinitions().SetOutOfControl(isOutOfControl)

    def SetPersistent(self, persistent):
        return self.CreateAttr().SetPersistent(persistent)

    def SetPlayerLookAtPos(self, targetPos, pitchStep, yawStep, blockInput=True):
        return self.CreateRot().SetPlayerLookAtPos(targetPos, pitchStep, yawStep, blockInput)

    def SetPos(self, pos):
        return self.CreatePos().SetPos(pos)

    def SetRecoverTotalAirSupplyTime(self, timeSec):
        return self.CreateBreath().SetRecoverTotalAirSupplyTime(timeSec)

    def SetRot(self, rot):
        return self.CreateRot().SetRot(rot)

    def SetSheared(self, isSheared):
        return self.CreateEntityDefinitions().SetSheared(isSheared)

    def SetSitting(self, shouldSitDown):
        return self.CreateEntityDefinitions().SetSitting(shouldSitDown)

    def SetSize(self, size):
        return self.CreateCollisionBox().SetSize(size)

    def SetTradeLevel(self, holderId):
        return self.CreateEntityDefinitions().SetTradeLevel(holderId)

    def SetVariant(self, variantType):
        return self.CreateEntityDefinitions().SetVariant(variantType)

    def isEntityInLava(self):
        return self.CreateAttr().isEntityInLava()

    def isEntityOnGround(self):
        return self.CreateAttr().isEntityOnGround()

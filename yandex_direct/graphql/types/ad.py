import graphene

from ..interfaces import DirectInterface


class AdTypeEnum(graphene.Enum):
    TEXT_AD = 'TEXT_AD'
    MOBILE_APP_AD = 'MOBILE_APP_AD'
    DYNAMIC_TEXT_AD = 'DYNAMIC_TEXT_AD'
    IMAGE_AD = 'IMAGE_AD'


class AdStatusEnum(graphene.Enum):
    ACCEPTED = 'ACCEPTED'
    DRAFT = 'DRAFT'
    MODERATION = 'MODERATION'
    REJECTED = 'REJECTED'
    PREACCEPTED = 'PREACCEPTED'
    UNKNOWN = 'UNKNOWN'


class AdType(DirectInterface):
    SERVICE = 'ads'

    CampaignId = graphene.Int()
    Status = AdStatusEnum()
    Type = AdTypeEnum()

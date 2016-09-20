import graphene

from ..interfaces import DirectInterface


class CampaignTypeEnum(graphene.Enum):
    TEXT_CAMPAIGN = 'TEXT_CAMPAIGN'
    MOBILE_APP_CAMPAIGN = 'MOBILE_APP_CAMPAIGN'
    DYNAMIC_TEXT_CAMPAIGN = 'DYNAMIC_TEXT_CAMPAIGN'
    UNKNOWN = 'UNKNOWN'


class CampaignStatusEnum(graphene.Enum):
    ACCEPTED = 'ACCEPTED'
    DRAFT = 'DRAFT'
    MODERATION = 'MODERATION'
    REJECTED = 'REJECTED'
    UNKNOWN = 'UNKNOWN'


class CampaignStatusPaymentEnum(graphene.Enum):
    DISALLOWED = 'DISALLOWED'
    ALLOWED = 'ALLOWED'


class CampaignType(DirectInterface):
    SERVICE = 'campaigns'
    Name = graphene.StringField()

    Type = graphene.StringField()
    Status = CampaignStatusEnum()
    StatusPayment = CampaignStatusPaymentEnum()

    # Relationships
    # ads = graphene.Field(graphene.List('AdType'))

    # def resolve_ads(campaign, args, info):
    #     return campaign.Id

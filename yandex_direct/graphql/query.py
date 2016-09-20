import graphene

from yandex_direct.init import call_api
from . import types


def get_field_names(info):
    fields = []
    for selectios in info.operation.selection_set.selections:
        if selectios.name.value == info.field_name:
            for selection in selectios.selection_set.selections:
                fields.append(selection.name.value)
    return fields


FILTERS_MAP = {
    'Id': 'Ids',
    'Status': 'Statuses',
    'State': 'States',
    'Type': 'Types',
    'StatusPayment': 'StatusesPayment',
    'CampaignId': 'CampaignIds',
}


def resolve_many(root, args, info):
    field_names = get_field_names(info)

    filters = {}
    for field, key in FILTERS_MAP.items():
        value = args.get(field)
        if value:
            filters[key] = [value]

    try:
        type_name = info.return_type.of_type.name
    except:
        type_name = info.return_type.name

    object_type = getattr(types, type_name)

    items = call_api(
        object_type.SERVICE,
        'get',
        params={
            'FieldNames': field_names,
            'SelectionCriteria': filters,
        }
    )
    return [
        object_type(**data)
        for data in items
    ]


def resolve_one(root, args, info):
    return resolve_many(root, args, info)[0]


class QueryType(graphene.ObjectType):
    name = 'Query'

    campaign = graphene.Field(
        types.CampaignType,
        Id=graphene.IntField(),
        resolver=resolve_one,
    )

    campaigns = graphene.ListField(
        types.CampaignType,
        Status=graphene.StringField(),
        resolver=resolve_many,
    )

    ad = graphene.Field(
        types.AdType,
        Id=graphene.IntField(),
        resolver=resolve_one,
    )

    ads = graphene.ListField(
        types.AdType,
        CampaignId=graphene.Int(),
        resolver=resolve_many,
    )

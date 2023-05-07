from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField

from quest.types import CategoryType, QuestType


class Query(ObjectType):
    category = relay.Node.Field(CategoryType)
    all_categories = DjangoFilterConnectionField(CategoryType)

    quest = relay.Node.Field(QuestType)
    all_quests = DjangoFilterConnectionField(QuestType)


    
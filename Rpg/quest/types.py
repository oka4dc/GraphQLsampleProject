from graphene import relay
from graphene_django import DjangoObjectType

from quest.models import Category, Quest


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['title', ]
        interfaces = (relay.Node,)


class QuestType(DjangoObjectType):
    class Meta:
        model = Quest
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains'],
            'category': ['exact'],
            'category__title': ['exact'],
        }
        interfaces = (relay.Node,)
import graphene
from graphene import Mutation

from quest.models import Category, Quest
from quest.types import CategoryType, QuestType


class UpdateCategory(Mutation):
    class Arguments:
        title = graphene.String(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()

        return UpdateCategory(category=category)


class CreateCategory(Mutation):
    class Arguments:
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()

        return CreateCategory(category=category)
    
class QuestInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
    category = graphene.Int()

class CreateQuest(graphene.Mutation):
    class Arguments:
        input = QuestInput(required=True)

    quest = graphene.Field(QuestType)

    @classmethod
    def mutate(cls, root, info, input):
        quest = Quest()
        quest.title = input.title
        quest.description = input.description
        quest.category_id = input.category
        quest.save()

        return CreateQuest(quest=quest)


class UpdateQuest(graphene.Mutation):
    class Arguments:
        input = QuestInput(required=True)
        id = graphene.ID()

    quest = graphene.Field(QuestType)

    @classmethod
    def mutate(cls, root, info, input, id):
        quest = Quest.objects.get(pk=id)
        quest.title = input.title
        quest.description = input.description
        quest.category_id = input.category
        quest.save()
        return UpdateQuest(quest=quest)
    
class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    update_quest = UpdateQuest.Field()
    create_quest = CreateQuest.Field()


    
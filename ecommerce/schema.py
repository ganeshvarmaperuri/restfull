import graphene
from graphene_django import DjangoObjectType
from .models import Book, Category, Grocery


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
            "title",
            "category",
            "author",
            "pages",
            "price",
            "quantity",
            "description",
            "date_created",
        )


class GroceryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = (
            "name",
            "product_tag",
            "category",
            "price",
            "quantity",
            "date_created",
        )


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    books = graphene.List(BookType)
    groceries = graphene.List(GroceryType)

    def resolve_book():
        pass
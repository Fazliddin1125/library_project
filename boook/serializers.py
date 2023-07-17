from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import BookModel


class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = BookModel
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price', )

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        print(title.isalpha())
        title_words = title.split()
        length = len(title.split())
        print(title_words)
        alpha = False
        # check title if it contains only alphabetical chars
        if length == 1:
            if title.isalpha():
                alpha = True

        else:
            for i in range(length):
                if title_words[i].isalpha():
                    print(title_words[i])
                    alpha = True

        if not alpha:
            print("alpha")
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak!"
                }
            )
        # check title and author from database existence
        if BookModel.objects.filter(title=title, author=author).exists():

            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz"
                }
            )

        return data


from rest_framework.viewsets import ModelViewSet

from .models import BookModel
from .serializers import BookSerializers
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

# class BookListApiView(ListAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializers

class BookListApiView(APIView):
    def get(self, request):
        try:
            books = BookModel.objects.all()
            serializer_data = BookSerializers(books, many=True).data
            data = {
                "satus": True,
                "books": serializer_data,
                "message": f"Returned {len(books)}"
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "message": "Not found",
                    "status": False
                }, status=status.HTTP_404_NOT_FOUND
            )

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializers

class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = BookModel.objects.get(id=pk)
            serializer_data = BookSerializers(book).data
            data = {
                "status": True,
                "book": serializer_data,
                "message": "Successfully"
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "Book is not found",

                },
                status=status.HTTP_404_NOT_FOUND
            )


# class BookDeleteApiView(generics.RetrieveDestroyAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializers

class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = BookModel.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    "message": "This book has just been deleted",
                    "status": True
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    "status": False,
                    "message": "Book is not fount"
                }, status=status.HTTP_400_BAD_REQUEST
            )



# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializers

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(BookModel.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializers(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            return Response(
                {"status": True, "message": f"Book {book_saved} update successfully"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "status": False, "message": "This data is fit"
                }, status=status.HTTP_400_BAD_REQUEST
            )

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializers


class BookCreateApiView(APIView):

    def post(self,  request):
        data = request.data
        serializer = BookSerializers(data=data)

        if serializer.is_valid():
            book = serializer.save()

            data = {
                "status": True,
                "book": data,
                'message': "This book has just been created"
            }
            return Response(data, status=status.HTTP_200_OK)
        else:

            return Response(
                {
                    'status': False,
                    'message': "Serializer is not valid"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class BookViewset(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers

@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = BookModel.objects.all()
    serializer = BookSerializers(books, many=True)
    return Response(serializer.data)
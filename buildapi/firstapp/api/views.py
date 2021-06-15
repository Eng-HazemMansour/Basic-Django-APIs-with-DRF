from rest_framework.response import Response
from firstapp.models import Note
from .serializers import NoteSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


#This class will list all notes if no param was given after the url --> http://localhost:8000/api/notes/
#In case you entered this url --> http://localhost:8000/api/notes/?title=title2 it will return the note which has 
#a title = "title2"
class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            title = request.query_params["title"]
            if title != None:
                queryset = Note.objects.get(title=title)
                serializer_class = NoteSerializer(queryset)
        except:
            queryset = self.get_queryset()
            serializer_class = NoteSerializer(queryset, many = True)

        return Response(serializer_class.data)



#This class can be used to retrieve a note using its ID --> http://localhost:8000/api/notes/1/
class NoteDetails(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



#This is a function and a class to create a new note --> http://localhost:8000/api/notes/create/
@api_view (["POST",])
def create(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success" : True,
            "message" : "Note is created successfully!"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success" : False,
        "error" : serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)



class NoteCreate(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



#This is a class to update a note --> http://localhost:8000/api/notes/update/1
class NoteUpdate(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


#This is a class to delete a note --> http://localhost:8000/api/notes/delete/1
class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

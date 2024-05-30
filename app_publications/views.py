import re
from time import time

from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from config import settings
from .filters import PaperFilters
from .permissions import IsSuperUserOrReadOnly
from .models import (
    SpheresModel,
    ReviewersModel,
    ReferencesModel,
    PublicationsModel,
    PapersModel,
    FeedbacksModel,
    RequirementsModel, FAQsModel, ContactsModel
)
from .serializers import (
    SphereSerializer, SphereGetSerializer,
    ReviewerSerializer, ReviewerGetSerializer,
    ReferencesSerializer,
    PublicationsSerializer, PublicationsGetSerializer,
    PapersSerializer, PapersGetSerializer,
    FeedbacksSerializer,
    RequirementSerializers, RequirementGetSerializers,
    FAQSerializers, FAQGetSerializers,
    ContactSerializers,
)


# Create your views here.
class SphereViewSet(ModelViewSet):
    queryset = SpheresModel.objects.all()
    # serializer_class = SphereSerializer
    permission_classes = [IsSuperUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SphereGetSerializer
        return SphereSerializer


class ReviewerViewSet(ModelViewSet):
    queryset = ReviewersModel.objects.all()
    # serializer_class = ReviewerSerializer
    permission_classes = [IsSuperUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewerGetSerializer
        return ReviewerSerializer


class ReferencesViewSet(ModelViewSet):
    queryset = ReferencesModel.objects.all()
    serializer_class = ReferencesSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class PublicationsViewSet(ModelViewSet):
    queryset = PublicationsModel.objects.all()
    permission_classes = [IsSuperUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PublicationsGetSerializer
        return PublicationsSerializer


class PapersViewSet(ModelViewSet):
    queryset = PapersModel.objects.all()
    permission_classes = [IsSuperUserOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PaperFilters

    def retrieve(self, request, pk=None, *args, **kwargs):
        title = f"paper_{pk}"
        if title in request.COOKIES:
            if time() - float(request.COOKIES[title]) > 3:
                up = True
            else:
                up = False
        else:
            up = True

        if up:
            paper_cv = PapersModel.objects.get(pk=pk).views_count
            PapersModel.objects.filter(pk=pk).update(views_count=paper_cv+1)
        response = super().retrieve(request, *args, **kwargs)
        response.set_cookie(title, time())
        return response

        # instance = PapersModel.objects.get(pk=kwargs['pk'])
        # instance.views_count += 1
        # instance.save()
        #
        # return super().retrieve(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PapersGetSerializer
        return PapersSerializer


class FeedbacksViewSet(ModelViewSet):
    queryset = FeedbacksModel.objects.all()
    serializer_class = FeedbacksSerializer
    permission_classes = [IsSuperUserOrReadOnly]


@api_view(['GET'])
def get_article(request, article_id):
    paper = PapersGetSerializer(PapersModel.objects.get(id=article_id))
    feedback = FeedbacksSerializer(FeedbacksModel.objects.filter(feedback_paper=article_id), many=True)

    return Response(
        data={
            "article": paper.data,
            "feedback": feedback.data
        },
        status=status.HTTP_200_OK
    )


class RequirementViewSet(ModelViewSet):
    queryset = RequirementsModel.objects.all()
    permission_classes = [IsSuperUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RequirementGetSerializers
        return RequirementSerializers

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


class FAQViewSet(ModelViewSet):
    queryset = FAQsModel.objects.all()
    permission_classes = [IsSuperUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FAQGetSerializers
        return FAQSerializers

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


# class ContactViewSet(ListCreateAPIView):
#     queryset = ContactsModel.objects.all()
#     serializer_class = ContactSerializers


@api_view(['GET', 'POST'])
def contact_view(request):
    if request.method == "POST":
        print(request.method)
        try:
            fullname = request.data['fullname']
            email = request.data['email']
            message = request.data['message']
        except KeyError:
            return Response(
                data={
                    "massage": "please, send us fullname, email, message",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            def validate_email(email):
                if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    return True
                return False

            if validate_email(email):
                send_mail(
                    subject=fullname,
                    from_email=email,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    message=f'{message}',
                )
                return Response(
                    data={
                        "message": "sent"
                    }
                )
            else:
                return Response(
                    data={
                        "message": "Invalid email address"
                    }
                )
        except:
            return Response({"message": "Something was wrong"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        return Response(
            data={
                "message": "OK"
            }
        )
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import (
    SpheresModel,
    ReviewersModel,
    ReferencesModel,
    PublicationsModel,
    PapersModel,
    FeedbacksModel,
    RequirementsModel,
    FAQsModel,
    ContactsModel,
)


class SphereSerializer(ModelSerializer):
    class Meta:
        model = SpheresModel
        fields = '__all__'


class SphereGetSerializer(ModelSerializer):
    sphere_name = SerializerMethodField(method_name='get_sphere_name', read_only=True)

    class Meta:
        model = SpheresModel
        fields = ('id', 'sphere_name')

    def get_sphere_name(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'en':
                return obj.sphere_name_en
            elif lang == 'ru':
                return obj.sphere_name_ru
            else:
                return obj.sphere_name_uz
        except KeyError:
            return obj.sphere_name_uz


class ReviewerSerializer(ModelSerializer):
    class Meta:
        model = ReviewersModel
        fields = '__all__'


class ReviewerGetSerializer(ModelSerializer):
    reviewer_position = SerializerMethodField(method_name='get_reviewer_position', read_only=True)

    class Meta:
        model = ReviewersModel
        fields = ['id', 'reviewer_name', 'reviewer_sphere', 'reviewer_position']

    def get_reviewer_position(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'en':
                return obj.reviewer_position_en
            elif lang == 'ru':
                return obj.reviewer_position_ru
            else:
                return obj.reviewer_position_uz
        except KeyError:
            return obj.reviewer_position_uz


class ReferencesSerializer(ModelSerializer):
    class Meta:
        model = ReferencesModel
        fields = '__all__'


class PublicationsSerializer(ModelSerializer):
    class Meta:
        model = PublicationsModel
        fields = '__all__'


class PublicationsGetSerializer(ModelSerializer):
    pub_name = SerializerMethodField(method_name='get_pub_name', read_only=True)
    pub_annotation = SerializerMethodField(method_name='get_pub_annotation', read_only=True)

    class Meta:
        model = PublicationsModel
        fields = ['id', 'pub_name', 'pub_image', 'pub_annotation', 'pub_sphere']

    def get_pub_name(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'en':
                return obj.pub_name_en
            elif lang == 'ru':
                return obj.pub_name_ru
            else:
                return obj.pub_name_uz
        except KeyError:
            return obj.pub_name_uz

    def get_pub_annotation(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'en':
                return obj.pub_annotation_en
            elif lang == 'ru':
                return obj.pub_annotation_ru
            else:
                return obj.pub_annotation_uz
        except KeyError:
            return obj.pub_annotation_uz


class PapersSerializer(ModelSerializer):
    class Meta:
        model = PapersModel
        fields = '__all__'


class PapersGetSerializer(ModelSerializer):
    paper_title = SerializerMethodField(method_name='get_paper_title', read_only=True)
    paper_annotation = SerializerMethodField(method_name='get_paper_annotation', read_only=True)

    class Meta:
        model = PapersModel
        fields = ['id', 'paper_sphere', 'paper_title', 'created_at', 'author',
                  'views_count', 'paper_annotation', 'paper_reference']

    def get_paper_title(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'en':
                return obj.paper_title_en
            elif lang == 'ru':
                return obj.paper_title_ru
            else:
                return obj.paper_title_uz
        except KeyError:
            return obj.paper_title_uz

    def get_paper_annotation(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'en':
                return obj.paper_annotation_en
            elif lang == 'ru':
                return obj.paper_annotation_ru
            else:
                return obj.paper_annotation_uz
        except KeyError:
            return obj.paper_annotation_uz


class FeedbacksSerializer(ModelSerializer):
    class Meta:
        model = FeedbacksModel
        fields = '__all__'


#  Requirements
class RequirementSerializers(ModelSerializer):
    class Meta:
        model = RequirementsModel
        fields = '__all__'


class RequirementGetSerializers(ModelSerializer):
    requirement_name = SerializerMethodField(method_name='get_requirement_name', read_only=True)
    requirement_desc = SerializerMethodField(method_name='get_requirement_desc', read_only=True)

    class Meta:
        model = RequirementsModel
        fields = ('id', 'requirement_name', 'requirement_desc')

    def get_requirement_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.req_name_en
            return obj.req_name_uz
        except:
            return obj.req_name_uz

    def get_requirement_desc(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.req_desc_en
            return obj.req_desc_uz
        except:
            return obj.req_desc_uz


# FAQs
class FAQSerializers(ModelSerializer):
    class Meta:
        model = FAQsModel
        fields = '__all__'


class FAQGetSerializers(ModelSerializer):
    faq_name = SerializerMethodField(method_name='get_faq_name', read_only=True)
    faq_ans = SerializerMethodField(method_name='get_faq_ans', read_only=True)

    class Meta:
        model = FAQsModel
        fields = ('id', 'faq_name', 'faq_ans')

    def get_faq_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.faq_name_en
            return obj.faq_name_uz
        except:
            return obj.faq_name_uz

    def get_faq_ans(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.faq_ans_en
            return obj.faq_ans_uz
        except:
            return obj.faq_ans_uz


class ContactSerializers(ModelSerializer):
    class Meta:
        model = ContactsModel
        fields = ('firstname', 'email', 'message')

from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.author

    class Meta:
        abstract = True
        db_table = 'abstract_model'


class SpheresModel(AbstractModel):
    sphere_name_uz = models.CharField(max_length=50)
    sphere_name_en = models.CharField(max_length=50)
    sphere_name_ru = models.CharField(max_length=50)

    def __str__(self):
        return self.sphere_name_uz

    class Meta:
        db_table = 'spheres'


class ReviewersModel(AbstractModel):
    reviewer_name = models.CharField(max_length=50)
    reviewer_position_uz = models.CharField(max_length=50)
    reviewer_position_en = models.CharField(max_length=50)
    reviewer_position_ru = models.CharField(max_length=50)
    reviewer_sphere = models.ManyToManyField(SpheresModel())

    def __str__(self):
        return self.reviewer_name

    class Meta:
        db_table = 'reviewers'


class ReferencesModel(AbstractModel):
    reference_name = models.CharField(max_length=50)

    def __str__(self):
        return self.reference_name

    class Meta:
        db_table = 'references'


class PublicationsModel(AbstractModel):
    pub_name_uz = models.CharField(max_length=50)
    pub_name_en = models.CharField(max_length=50)
    pub_name_ru = models.CharField(max_length=50)
    pub_annotation_uz = models.TextField()
    pub_annotation_en = models.TextField()
    pub_annotation_ru = models.TextField()
    pub_image = models.ImageField(upload_to='static/pub_image/')
    pub_sphere = models.ManyToManyField(SpheresModel())

    def __str__(self):
        return self.pub_name_uz

    class Meta:
        db_table = 'publications'


class PapersModel(AbstractModel):
    paper_title_uz = models.CharField(max_length=50)
    paper_title_en = models.CharField(max_length=50)
    paper_title_ru = models.CharField(max_length=50)
    paper_annotation_uz = models.CharField(max_length=500)
    paper_annotation_en = models.CharField(max_length=500)
    paper_annotation_ru = models.CharField(max_length=500)
    views_count = models.IntegerField(default=0)
    keyword = models.CharField(max_length=100)
    paper_sphere = models.ForeignKey(SpheresModel(), on_delete=models.CASCADE)
    paper_pub = models.ForeignKey(PublicationsModel(), on_delete=models.CASCADE)
    paper_reference = models.ManyToManyField(ReferencesModel())

    def __str__(self):
        return self.paper_title_uz

    class Meta:
        db_table = 'papers'


class FeedbacksModel(AbstractModel):
    feedback_paper = models.ForeignKey(PapersModel(), on_delete=models.CASCADE)
    feedback_reviewer = models.ForeignKey(ReviewersModel(), on_delete=models.CASCADE)
    feedback_file = models.FileField(upload_to='static/feedback/')

    def __str__(self):
        return self.feedback_paper

    class Meta:
        db_table = 'feedbacks'


class RequirementsModel(AbstractModel):
    req_name_uz = models.CharField(max_length=255)
    req_name_en = models.CharField(max_length=255)
    req_description_uz = models.TextField()
    req_description_en = models.TextField()

    def __str__(self):
        return self.req_name_uz

    class Meta:
        db_table = 'requirements'


class FAQsModel(AbstractModel):
    faq_question_uz = models.CharField(max_length=255)
    faq_question_en = models.CharField(max_length=255)
    faq_answer_uz = models.TextField()
    faq_answer_en = models.TextField()

    def __str__(self):
        return self.faq_answer_uz

    class Meta:
        db_table = 'FAQs'


class ContactsModel(AbstractModel):
    firstname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = 'contacts'

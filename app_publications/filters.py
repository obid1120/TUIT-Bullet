import django_filters
from django_filters import FilterSet

from .models import PapersModel


class PaperFilters(FilterSet):
    paper_title_uz = django_filters.CharFilter(lookup_expr='exact')
    paper_title_en = django_filters.CharFilter(lookup_expr='exact')
    paper_title_ru = django_filters.CharFilter(lookup_expr='exact')
    author = django_filters.CharFilter(lookup_expr='exact')
    keyword = django_filters.CharFilter(lookup_expr='exact')
    paper_sphere = django_filters.NumberFilter(lookup_expr='exact')
    paper_reference = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = PapersModel
        fields = ['paper_title_uz', 'paper_title_en', 'paper_title_ru', 'author',
                  'keyword', 'paper_sphere', 'paper_reference']

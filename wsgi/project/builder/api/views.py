from rest_framework import viewsets

from ..models import Section, Block
from .serializers import SectionSerializer, BlockSerializer #, BlockSerializer

# ViewSets define the view behavior.
class BlockViewSet(viewsets.ModelViewSet):
  queryset = Block.objects.none()
  serializer_class = BlockSerializer

  def get_queryset(self):
    queryset = Block.objects.none()
    section_id = self.request.query_params.get('section_id', None)
    if section_id is not None:
        queryset = Block.objects.filter(section_id=section_id)
    return queryset.order_by('order', 'id')

class SectionViewSet(viewsets.ModelViewSet):
  queryset = Section.objects.none()
  serializer_class = SectionSerializer

  def get_queryset(self):
    queryset = Section.objects.all()
    return queryset.order_by('order', 'id')

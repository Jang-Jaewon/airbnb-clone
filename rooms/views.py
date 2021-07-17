from django.utils import timezone
from django.views.generic import ListView
from . import models


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 10  # 👈 한 페이지에 제한할 Object 수
    paginate_orphans = 5  # 👈 짜투리 처리
    ordering = "created"  # 👈 정렬 기준
    page_kwarg = "page"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # 기존의 CBV에서 만들어진 것을 가져옵니다:)
        now = timezone.now()
        context["now"] = now
        return context

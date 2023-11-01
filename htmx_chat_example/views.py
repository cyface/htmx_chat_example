"""
Views
"""

from django.views.generic.base import TemplateResponseMixin, View

from htmx_chat_example.models import Message


class ChatView(View, TemplateResponseMixin):
    template_name = "components/chat.html"

    channel_pk = 1

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        Message.objects.create(
            channel_id=self.channel_pk,
            content=request.POST.get("message"),
            from_user_id=request.user.pk
        )
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = {
            "channel_pk": self.channel_pk,
            "messages": Message.objects.filter(
                channel=self.channel_pk
            ).order_by(
                "created_at"
            )
        }
        return context

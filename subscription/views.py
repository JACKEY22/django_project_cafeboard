from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from article.models import Article
from shop.models import Shop
from subscription.models import Subscription


@method_decorator(login_required(login_url='account:login'), 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('shop:detail', kwargs={'pk':self.request.GET.get('shop_pk')})

    def get(self, request, *args, **kwargs):

        shop = get_object_or_404(Shop, pk=self.request.GET.get('shop_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, shop=shop)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, shop=shop).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required(login_url='account:login'), 'get')
class SubscriptionListView(ListView):
    model = Article
    template_name = 'subscription/list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        target_user = Subscription.objects.filter(user=self.request.user).values_list('target_user')
        article_list = Article.objects.filter(writer__in=target_user)

        return article_list

class SubscriptionFollowView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('account:detail', kwargs={'pk': self.request.GET.get('target_user_pk')})

    def get(self, request, *args, **kwargs):

        target_user = get_object_or_404(User, pk=self.request.GET.get('target_user_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, target_user=target_user)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, target_user=target_user).save()

        return super(SubscriptionFollowView, self).get(request, *args, **kwargs)

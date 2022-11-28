from django.shortcuts import render
from django.views.generic import TemplateView

import json
from django.shortcuts import redirect

class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_title'] = 'заголовок новости'
        context['news_text'] = 'Новость ни о чём. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Esse, est rerum minus cum consequuntur totam dolores adipisci quaerat praesentium iusto?'
        context['range'] = range(5)

        with open('./static/News.json', 'r', encoding='utf-8') as news_file:
            context['news_json'] = json.load(news_file)

        return context

class NewsPageViewPaginator(NewsPageView):

    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = page
        return context


class NewsPageViewSearch(NewsPageView):

    def redirectToSearch(request, text):
        return redirect(f'https://yandex.ru/search/?text={text}')
        

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
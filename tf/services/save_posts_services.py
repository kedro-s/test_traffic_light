from django.core.exceptions import ObjectDoesNotExist
from tf.models import *


class SavePostsService:
    def save_posts(self, responce):
        for post in responce:
            try:
                user = User.objects.get(pk=post['userId'])
                p = Post()
                p.user = user
                p.id = post['id']
                p.title = post['title']
                p.body = post['body']
                p.save()
            except ObjectDoesNotExist:
                pass
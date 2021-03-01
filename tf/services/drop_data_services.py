from tf.models import *


class DropDataService:
    def drop_data(self):
        Post.objects.all().delete()
        User.objects.all().delete()
        Company.objects.all().delete()
        Company.objects.all().delete()
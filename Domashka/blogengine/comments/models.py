from django.db import models

# Create your models here.

class COMMENTS(models.Model):
    blog_id = models.TextField(blank=True, db_index=True)
    body_comment = models.TextField(blank=True, db_index=True)

    
    def get_id_comments(id):
        ccc = COMMENTS.objects.all()
        comments_for_this = list()
        for comm_ in ccc:
            if comm_.blog_id == id: #self.id
                comments_for_this.append(comm_.body_comment)

        return comments_for_this

    def for_read(self): 
        return '{}'.format(self.blog_id)
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#
#     def __str__(self):
#         return self.title


class Comment1(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

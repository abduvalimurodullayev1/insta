import uuid

from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save,post_delete
from django.utils.text import slugify
from django.urls import reverse


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name="Tag")
    slug = models.SlugField(null=False, unique=True, default=uuid.uuid1)


class Meta:
    verbose_name = 'Tag'
    verbose_name_plural = 'Tags'


def get_absolute_url(self):
    return reverse('tags', args=[self.slug])

def __str__(self):
    return self.title

def save(self, *args,**kwargs):
    if not self.slug:
        self.slug - slugify(self.slug)
        return super().save(*args,**kwargs)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(upload_to=user_directory_path,verbose_name="Picture", null=True)
    caption = models.CharField(max_length=1000000, verbose_name='Caption')
    posted = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name='tags')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)


def get_absolute_url(self):
    return reverse('post-details', args=[str(self.id)])


def __str__(self):
    return self.caption


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')


class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()

    def add_post(sender, instance, *args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)

        for follower in followers:
            stream = Stream(post=post, user=follower.follower, date=post.posted, following=user)
            stream.save()
post_save.connect(Stream.add_post,sender=Post)


class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_likes')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_likes')




from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)  # CharField는 길이 제한
    content = models.TextField()   # TextField는 길이 제한 없음
    created_at = models.DateTimeField(auto_now_add=True)
    

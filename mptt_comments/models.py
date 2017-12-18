import datetime

from django.db import models
from django_comments.models import Comment
from django.core import urlresolvers

from mptt.models import MPTTModel
from mptt_comments.managers import MpttCommentManager

class AbstractMpttComment(MPTTModel, Comment):

    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True)
    
    def save(self, *a, **kw):
        if not self.ip_address:
            self.ip_address = '0.0.0.0'
        super(AbstractMpttComment, self).save(*a, **kw)
        
    def get_absolute_url(self, anchor_pattern="#c%(id)s"):
        tree_url = urlresolvers.reverse("comment-detail-tree", args=(self.tree_id, ))
        return "%s#c%s" % (tree_url, self.id)
    
    class Meta:
        abstract = True
        ordering = ('tree_id', 'lft')

class MpttComment(AbstractMpttComment):
    
    objects = MpttCommentManager()

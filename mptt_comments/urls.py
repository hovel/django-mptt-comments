from django.conf.urls import url
from django_comments.urls import urlpatterns as contrib_comments_urlpatterns
from mptt_comments import views

urlpatterns = [
    url(r'^new/(\d+)/$',
        views.new_comment,
        name='new-comment'
    ),
    url(r'^reply/(?P<parent_pk>\d+)/$',
        views.new_comment,
        name='comment-reply'
    ),
    url(r'^new_comment/(?P<content_type>[\w.]+)/(?P<object_pk>\d+)/$',
        views.new_comment,
        name='comment-toplevel-reply'
    ),
    url(r'^post/$',
        views.post_comment,
        name='comments-post-comment'
    ),
    url(r'^posted-ajax/$',
        views.comment_done_ajax,
        name='comments-comment-done-ajax'
    ),
    url(r'^more/(\d+)/$',
        views.comments_more,
        name='comments-more'
    ),
    url(r'^more-in-tree/(\d+)/$',
        views.comments_more,
        name='comments-more-in-tree',
        kwargs={'restrict_to_tree': True}
    ),
    url(r'^replies/(\d+)/$',
        views.comments_subtree,
        name='comments-subtree'
    ),
    url(r'^detail/(\d+)/$',
        views.comments_subtree,
        name='comment-detail',
        kwargs={'include_self': True, 'include_ancestors': True}
    ),
    url(r'^tree/(\d+)/$',
        views.comments_fulltree,
        name='comment-detail-tree',
    ),
    url(r'^count/(\d+)/(\d+)/$',
        views.count_for_object,
        name='comments-count'
    )
]

urlpatterns += contrib_comments_urlpatterns

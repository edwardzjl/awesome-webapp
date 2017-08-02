# handlers.py

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post
from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    summary = 'Go fuck yourself.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='hahaha', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='asdgjbhawerg', summary=summary, created_at=time.time()-7200)
    ]
    return {
            '__template__': 'blogs.html',
            'blogs': blogs
    }

@get('/api/users')
async def api_get_users():
    users = await User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd='******'
    return dict(users=users)


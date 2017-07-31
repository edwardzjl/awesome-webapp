import orm, asyncio, logging
from models import User, Blog, Comment


loop = asyncio.get_event_loop()


async def test():
    await orm.create_pool(loop, user='edwardlol', password='900315', database='ed_playg')

    u = User(name='test', email='test@example.com', passwd='1234567', image='about:blank')

    await u.save()

loop.run_until_complete(test())
loop.close()

from utils.web.tools import redirect


def login_required(func):
    """ Allow only auth users """
    async def wrapped(request, *args, **kwargs):

        if request.user is None:
            redirect(request, 'login', **kwargs)
        return await func(request, *args, **kwargs)
    return wrapped

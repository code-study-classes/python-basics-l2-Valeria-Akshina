from functools import reduce


def update_profile(user_id, **kwargs):
    return {'id': user_id, 'updated_fields': kwargs}

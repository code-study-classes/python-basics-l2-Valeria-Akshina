def update_profile(user_id, **kwargs):
    return {'id': user_id, 'updated_fields': kwargs}

def get_domains(emails):
    return map(lambda email: email.split('@')[1], emails)

def filter_target_audience(users):
    return filter(lambda user: user['age'] >= 18 and user['is_premium'], users)
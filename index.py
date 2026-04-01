def update_profile(user_id, **kwargs):
    return {'id': user_id, 'updated_fields': kwargs}

def get_domains(emails):
    return map(lambda email: email.split('@')[1], emails)

def filter_target_audience(users):
    return filter(lambda user: user['age'] >= 18 and user['is_premium'], users)

def build_response(status_code, *errors, **payload):
    return {'status': status_code, 'errors': errors, 'data': payload}

def calculate_total_spent(transactions):
    total = 0
    for transaction in transactions:
        total = total + transaction['amount']
    return total
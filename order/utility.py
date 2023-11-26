import uuid


def get_tracking_number():
    return str(uuid.uuid4()).replace('-', '')[:10]

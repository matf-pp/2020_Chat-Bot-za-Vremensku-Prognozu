from datetime import datetime

def get_current_time() -> str:
    datetime_obj = datetime.now()
    current_time = datetime_obj.strftime('%d-%b-%Y : %H:%M:%S')
    return current_time
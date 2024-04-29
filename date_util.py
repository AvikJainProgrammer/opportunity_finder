# file: date_util.py
from datetime import datetime, timedelta

class DateUtil:
    @staticmethod
    def get_current_date_str():
        """Returns the current date as a string in 'YYYY-MM-DD' format."""
        return datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def get_date_with_offset(days=0):
        """Returns a date with an offset (in days) from today as a string in 'YYYY-MM-DD' format."""
        offset_date = datetime.now() + timedelta(days=days)
        return offset_date.strftime('%Y-%m-%d')

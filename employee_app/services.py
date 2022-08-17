import datetime
import os
from django.db import connection, IntegrityError


class ServiceEmployment(object):

    def __init__(self, active_tab=None, sub_active_tab=None):
        self.active_tab = active_tab
        self.sub_active_tab = sub_active_tab
        self.cursor = connection.cursor()

    def __del__(self):
        self.cursor.close()

    def test(self):
        try:
            query = 'SELECT * FROM admin_app_promotion order by created_time desc;'

            self.cursor.execute(query, )
            result = self.cursor.fetchall()

            row_headers = [col[0] for col in self.cursor.description]
            data = [dict(zip(row_headers, row)) for row in result]

            if len(result) > 0:
                return data
            else:
                return ReturnResponse.get_response(toast_type='info',
                                                   toast_message='No data found!')
        except IntegrityError:
            return ReturnResponse.get_response(is_success=False, toast_message='Username already exists!')
        finally:
            return ReturnResponse.get_response(is_success=False,
                                               toast_message='Something went wrong! Please try again.')


class ReturnResponse(object):

    @staticmethod
    def get_response(user_name=None, is_success=True,
                     toast_type=None, toast_message='', data=None):
        return {
            'user_name': user_name,
            'is_success': is_success,
            'toast_type': toast_type,
            'toast_message': toast_message,
            'data': data
        }

    @staticmethod
    def str_to_bool(is_recommended):
        if is_recommended == 'True':
            return True
        elif is_recommended is None:
            return False
        else:
            raise ValueError

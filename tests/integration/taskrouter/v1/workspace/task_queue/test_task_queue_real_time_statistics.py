# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class TaskQueueRealTimeStatisticsTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .task_queues("WQXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .real_time_statistics().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TaskQueues/WQXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/RealTimeStatistics',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "longest_task_waiting_age": 100,
                "longest_task_waiting_sid": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "longest_relative_task_age_in_queue": 100,
                "longest_relative_task_sid_in_queue": "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "tasks_by_status": {
                    "reserved": 0,
                    "pending": 0,
                    "assigned": 0,
                    "wrapping": 0
                },
                "total_eligible_workers": 100,
                "activity_statistics": [
                    {
                        "friendly_name": "Idle",
                        "workers": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "friendly_name": "Busy",
                        "workers": 9,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "friendly_name": "Offline",
                        "workers": 6,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "friendly_name": "Reserved",
                        "workers": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "tasks_by_priority": {},
                "total_tasks": 100,
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "total_available_workers": 100,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RealTimeStatistics"
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_queues("WQXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .real_time_statistics().fetch()

        self.assertIsNotNone(actual)

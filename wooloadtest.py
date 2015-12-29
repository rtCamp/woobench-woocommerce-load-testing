from locust import HttpLocust, TaskSet, task
from woocommerce import API

class WooLocust(HttpLocust):
    """
    This is the abstract Locust class which should be subclassed. It provides an XML-RPC client
    that can be used to make XML-RPC requests that will be tracked in Locust's statistics.
    """
    def __init__(self):
        self.client = API(
            url="http://dev.linuxontheheads.com",
            consumer_key="ck_84946169aed02894f3f53483432c339605f997a0",
            consumer_secret="cs_f9fbd218a9618201ae1aa841f19c0435f1a41440"
            )
class UserBehavior(TaskSet):
    def on_start(self):
        pass

    @task(1)
    def createorder(self):
        data = {
            "order": {
                "payment_details": {
                    "method_id": "bacs",
                    "method_title": "Direct Bank Transfer",
                    "paid": True
                },
                "billing_address": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "address_1": "969 Market",
                    "address_2": "",
                    "city": "San Francisco",
                    "state": "CA",
                    "postcode": "94103",
                    "country": "US",
                    "email": "john.doe@example.com",
                    "phone": "(555) 555-5555"
                },
                "shipping_address": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "address_1": "969 Market",
                    "address_2": "",
                    "city": "San Francisco",
                    "state": "CA",
                    "postcode": "94103",
                    "country": "US"
                },
                "customer_id": 2,
                "line_items": [
                    {
                        "product_id": 56,
                        "quantity": 2
                    },
                    {
                        "product_id": 70,
                        "quantity": 1,
                        "variations": {
                            "pa_color": "Black"
                        }
                    }
                ],
                "shipping_lines": [
                    {
                        "method_id": "flat_rate",
                        "method_title": "Flat Rate",
                        "total": 10
                    }
                ]
            }
        }
        self.client.post("/orders", data)

class ApiUser(WooLocust):
    host = "http://dev.linuxontheheads.com"
    task_set = UserBehavior
    min_wait=1

from locust import HttpLocust, TaskSet, task
import string 
import random
import time

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        #self.comment()

    @task(1)
    def comment(self):
        from splinter import Browser

        with Browser('phantomjs') as browser:   	  
	    foo = ['70', '37', '53', '31', '56', '50' , '19', '73', '76', '93', '99', '47', '34', '79', '60', '15', '96', '90', '87', '83', '67']
	# Visit URL
            url = WebsiteUser.host + "shop/?add-to-cart=" + random.choice(foo)
            browser.visit(url)
	    url = WebsiteUser.host + "checkout/"
            browser.visit(url)
 #           browser.fill('billing_email', 'hello@dfdf.dfdfdfdf')
    # Find and click the 'Place Order' button
            button = browser.find_by_name('woocommerce_checkout_place_order')
    # Interact with elements
            button.click()

#	    browser.quit()
class WebsiteUser(HttpLocust):
    host = "http://wootest.rtcamp.net/"
    weight = 1
    task_set = UserBehavior
#    min_wait=5000
#    max_wait=9000

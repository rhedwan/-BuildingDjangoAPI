from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'


class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'


""" 
<<<<<<<<<<<<<<<<<<<< Scoping Throttling >>>>>>>>>>>>>>>>>>>>>>
This would limit the number of request made on that endpoint depeding on the 
value provided in the settings.  
"""
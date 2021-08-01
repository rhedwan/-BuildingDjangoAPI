from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class WatchListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'videos'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'startfrom'


"""
<<<<<<<<<<<<<<<<<<<<< PageNumberPagination >>>>>>>>>>>>>>>>>>>>>>
LINKS: https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination,
https://www.django-rest-framework.org/api-guide/pagination/#configuration

    ------------- Overwriting Of Default Attributes ------------------
1. The 'page_size' is an attribute used for limiting the number of objects to be dispplayed.
2. The 'page_query_param' is an attribute used for renaming the endpoint query name
3. The 'page_size_query_param' is an attribute which gives the clients the power to determine 
it own page size.
    NOTE: It is passed as a parameter on "POSTMAN"
4. The 'max_page_size' is an attribute which can be used to block the access of large number 
passed by the clients. Hence, it overwrites the larger number passed by clients. 
5. The 'last_page_strings' is an attribute which is used to set a string for the last-page
    NOTE: By defaults it is 'last'


<<<<<<<<<<<<<<<<<<<< LimitOffsetPagination >>>>>>>>>>>>>>>>>>>>>
LINKS: https://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination,
https://www.django-rest-framework.org/api-guide/pagination/#configuration_1

    ------------- Overwriting Of Default Attributes ------------------

NOTE:'limit' is basically 'page size'
    'offset' is simply the number of records you wish to skip before selecting records. i.e 
    If offset = 10. It means we will skip first 10 elements and load result from 11
    Also, if limit = 10 and offset = 2:
    It means load 10 objects after the 2nd objects.

"""
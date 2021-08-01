from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'videos'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'

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
"""
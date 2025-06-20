# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Call Retail API to search for a products in a catalog,
# limit the number of the products per page and go to the next page using "next_page_token"
# or jump to chosen page using "offset".
#

# [START retail_search_for_products_with_pagination]

import google.auth
from google.cloud.retail import SearchRequest, SearchServiceClient

project_id = google.auth.default()[1]


# get search service request:
def get_search_request(query: str, page_size: int, offset: int, next_page_token: str):
    default_search_placement = (
        "projects/"
        + project_id
        + "/locations/global/catalogs/default_catalog/placements/default_search"
    )

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.visitor_id = "123456"  # A unique identifier to track visitors
    search_request.query = query
    search_request.page_size = page_size
    search_request.offset = offset
    search_request.page_token = next_page_token

    print("---search request:---")
    print(search_request)

    return search_request


# call the Retail Search:
def search():
    # TRY DIFFERENT PAGINATION PARAMETERS HERE:
    page_size = 6
    offset = 0
    page_token = ""

    search_request_first_page = get_search_request(
        "Hoodie", page_size, offset, page_token
    )
    search_response_first_page = SearchServiceClient().search(search_request_first_page)

    print("---search response---")
    if not search_response_first_page.results:
        print("The search operation returned no matching results.")
    else:
        print(search_response_first_page)

    # PASTE CALL WITH NEXT PAGE TOKEN HERE:

    # PASTE CALL WITH OFFSET HERE:

    return search_response_first_page


search()

# [END retail_search_for_products_with_pagination]

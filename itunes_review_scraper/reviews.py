from requests import codes as status
from .constants import Sort
from .utils import Requests
from .format import review_url, Reviews


class _ContinuationToken:
    __slots__ = "country", "sort", "page", "count"

    def __init__(self, country, sort, page, count):
        self.country = country
        self.sort = sort
        self.page = page
        self.count = count


def reviews(
    app_id: str,
    country: str,
    sort: Sort,
    count: int = 500,
    continuation_token: _ContinuationToken = None
):
    if continuation_token is not None:
        country = continuation_token.country
        sort = continuation_token.sort
        _fetched_page = continuation_token.page
        _count_to_fetch = continuation_token.count
    else:
        _count_to_fetch = count
        _fetched_page = 0
    
    review = []

    while True:
        if _count_to_fetch <= 0:
            break
        
        _fetched_page += 1

        url = review_url(country, _fetched_page, app_id, sort)
        result = Requests.get(url)

        if result.status_code == status.ok:
            for r in Reviews(result.text).get():
                review.append(r)
            
            _count_to_fetch = count - len(review)

    return (
        review,
        _ContinuationToken(country, sort, _fetched_page, count)
    )
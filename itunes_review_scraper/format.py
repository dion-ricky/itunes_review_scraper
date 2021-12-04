import json

from .constants import Sort
from .models import Review


def review_url(
    country: str,
    page: int,
    app_id: str,
    sort: Sort
):
    base_url = "https://itunes.apple.com/{country}/rss/customerreviews/page={page}/id={app_id}/sortby={sort}/json"

    return base_url.format(
        country=country,
        page=page,
        app_id=app_id,
        sort=sort.value
    )


class Reviews:
    __slots__ = "text_response", "review"

    def __init__(self, text_response: str):
        if type(text_response) != str:
            raise Exception("Expected <class 'str'> got {}".format(type(text_response)))

        self.text_response = text_response

    def get(self):
        reviews = self._parse_review()

        for review in reviews:
            yield Review(**review)
        
    def _parse_review(self):
        review_dict = json.loads(self.text_response)        
        
        for review in review_dict['feed']['entry']:
            yield Reviews._flatten_review(review)
    
    def _flatten_review(review):
        r = review

        flat = {
            'author_uri': r['author']['uri']['label'],
            'author_name': r['author']['name']['label'],
            'updated_date': r['updated']['label'],
            'rating': r['im:rating']['label'],
            'app_version': r['im:version']['label'],
            'review_id': r['id']['label'],
            'title': r['title']['label'],
            'content': r['content']['label'],
            'vote_sum': r['im:voteSum']['label'],
            'vote_count': r['im:voteCount']['label']
        }
        
        return flat
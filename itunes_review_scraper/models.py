

class Review(dict):
    __slots__ = "author_uri", "author_name", "updated_date", "rating", \
        "app_version", "review_id", "title", "content", "vote_sum", \
        "vote_count"

    def __init__(
        self,
        author_uri: str,
        author_name: str,
        updated_date: str,
        rating: int,
        app_version: str,
        review_id: str,
        title: str,
        content: str,
        vote_sum: int,
        vote_count: int
    ):
        dict.__init__(
            self,
            author_uri = author_uri,
            author_name = author_name,
            updated_date = updated_date,
            rating = rating,
            app_version = app_version,
            review_id = review_id,
            title = title,
            content = content,
            vote_sum = vote_sum,
            vote_count = vote_count
        )
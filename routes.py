from flask_restx import Resource

from main import FlaskRestApi
from schemas import tweet_data_model, tweet_response_model


@FlaskRestApi.route("/api/tweets")
class TweetResource(Resource):
    @FlaskRestApi.expect(tweet_data_model, validate=True) # что ожидает получить
    @FlaskRestApi.response(200, "Success", tweet_response_model) # что возвращает
    @FlaskRestApi.doc(description="Create a new tweet") # просто документация
    def post(self):
        """
        Create a new tweet
        """

        response_data = {
            "result": True,
            "tweet_id": 1,
        }
        return response_data, 200


    def get(self):
        response_data = {
            "result": True,
            "tweets": [
                {
                    "id": 0,
                    "content": "string",
                    "attachments": [
                        "string"
                    ],
                    "author": {
                        "id": 0,
                        "name": "string"
                    },
                    "likes": [
                        {
                            "user_id": 0,
                            "name": "string"
                        }
                    ]
                }
            ]
        }
        return response_data, 200

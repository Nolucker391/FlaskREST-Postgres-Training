from flask import Flask, request
from flask_restx import Api, Resource

from schemas import tweet_data_model, tweet_response_model
from models import Base, engine, Session

app = Flask(__name__)
FlaskRestApi = Api(app, version="1.0", title="Twitter Service API", description="API for MicroBlogging service")

FlaskRestApi.models['TweetData'] = tweet_data_model
FlaskRestApi.models['TweetResponse'] = tweet_response_model


@FlaskRestApi.route("/api/tweets")
class TweetResource(Resource):
    @FlaskRestApi.expect(tweet_data_model, validate=True)  # что ожидает получить
    @FlaskRestApi.response(200, "Success", tweet_response_model)  # что возвращает
    @FlaskRestApi.doc(description="Create a new tweet")  # просто документация
    def post(self):
        """
        Create a new tweet
        """
        api_key = request.headers.get("api-key")
        data = request.json

        response_data = {
            "api": api_key,
            "data": data,
        }
        return response_data, 200

    def get(self):
        data = request.data
        session = Session
        return f"This data: {data},</br> This session: {session}", 200


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True, host="0.0.0.0", port=8000)

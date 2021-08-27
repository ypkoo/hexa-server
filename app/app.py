from http import HTTPStatus

from flask import Flask, request, abort
import boto3
from pynamodb.models import DoesNotExist
from pynamodb.exceptions import DeleteError, PutError, UpdateError

import redis

from models import HexaSleepResultModel
from params_schema import CreateSessionSchema, UpdateSessionSchema
from configs import AUDIO_BUCKET


s3_client = boto3.client('s3')
create_session_schema = CreateSessionSchema()
update_session_schema = UpdateSessionSchema()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post('/status/<int:room_id>')
def update_status():
    pass

@app.post('/session')
def create_session():
    data = request.form
    errors = create_session_schema.validate(data)

    if errors:
        abort(HTTPStatus.BAD_REQUEST)
    args = create_session_schema.load(data)

    room_id = args.get('room_id')
    start_timestamp = args.get('start_timestamp')

    hexa_sleep_result = HexaSleepResultModel(hash_key=room_id, range_key=start_timestamp)

    try:
        hexa_sleep_result.save()
    except PutError as e:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)


@app.put('/session')
def update_session():
    data = request.form
    errors = update_session_schema.validate(data)

    if errors:
        abort(HTTPStatus.BAD_REQUEST)

    args = update_session_schema.load(data)

    room_id = args.get('room_id')
    start_timestamp = args.get('start_timestamp')
    seq_num = args.get('seq_num')
    audio_file = request.files['audio']

    try:
        hexa_sleep_result = HexaSleepResultModel.get(hash_key=room_id, range_key=start_timestamp)
        hexa_sleep_result.update(actions=[
            HexaSleepResultModel.last_seq_num.set(seq_num),
        ])
    except DoesNotExist as e:
        abort(HTTPStatus.NOT_FOUND)
    except UpdateError as e:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    s3_client.upload_fileobj(audio_file, AUDIO_BUCKET, f'{room_id}/{start_timestamp}/{seq_num}.wav')
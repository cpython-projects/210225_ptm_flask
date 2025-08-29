from flask import jsonify
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.models import db
import random
from app import create_app
from app.errors.question_errors import QuestionEmptyError, QuestionValueError, QuestionError


app = create_app()


errors = ['Котик думает', 'Котик что-то тормозит', 'Котик застрял']


# @app.errorhandler(QuestionEmptyError)
# def handle_validation_error(e):
#     # return jsonify({"error": e.errors()}), 400
#     return jsonify({'errors': str(e.message)}), 400
#
#
# @app.errorhandler(QuestionValueError)
# def handle_validation_error(e):
#     # return jsonify({"error": e.errors()}), 400
#     return jsonify({'errors': str(e.message)}), 400

@app.errorhandler(QuestionError)
def handle_validation_error(e):
    # return jsonify({"error": e.errors()}), 400
    return jsonify({'errors': str(e.message)}), 400

@app.errorhandler(ValidationError)
def handle_validation_error(e):
    # return jsonify({"error": e.errors()}), 400
    return jsonify({'errors': random.choice(errors)}), 400


@app.errorhandler(SQLAlchemyError)
def handle_db_error(e):
    db.session.rollback()
    return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
"""Utils for simplify using mongo database"""


def jsonify_mongodb_object(db_object: {}) -> {}:
    """
       Convert from database document to serializable object
       :param db_object: object from database
       :return: object ready to json'ify
       """
    if type(db_object) == tuple and '_id' not in db_object:
        return None
    else:
        db_object['_id'] = str(db_object['_id'])
        return db_object

from .entities.User import User

class ModelUser:

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            query = """ SELECT id, username, password, full_name FROM users
                        WHERE username = `{}`
                    """.format(user.username)
            
            cursor.execute(query)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)
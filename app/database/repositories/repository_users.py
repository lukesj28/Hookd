import psycopg2

from app.database.db import get_conn, put_conn


def create_user(email, username, image):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO hookd.users (email, username, image) VALUES (%s, %s, %s)"
            cur.execute(sql, (email, username, image))
            conn.commit()
            return {"success": True}
    except psycopg2.IntegrityError as err:
        conn.rollback()
        if err.pgcode == "23505":
            msg = err.diag.constraint_name
            if msg == "users_email_uk":
                return {"success": False, "error": "Email already in use"}
            elif msg == "users_username_uk":
                return {"success": False, "error": "Username already in use"}
        return {"success": False, "error": f"Something went wrong: {err}"}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_user(user_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT username, image FROM hookd.users WHERE user_id = %s"
            cur.execute(sql, (user_id,))
            row = cur.fetchone()
            if row:
                data = {"username": row[0], "image": row[1]}
                return {"success": True, "data": data}
            else:
                return {"success": False, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_user_id_by_email(email):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT user_id FROM hookd.users WHERE email = %s"
            cur.execute(sql, (email,))
            row = cur.fetchone()
            if row:
                return {"success": True, "data": row[0]}
            else:
                return {"success": False, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_user_id_by_username(username):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT user_id FROM hookd.users WHERE username = %s"
            cur.execute(sql, (username,))
            row = cur.fetchone()
            if row:
                return {"success": True, "data": row[0]}
            else:
                return {"success": False, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_email_by_user_id(user_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT email FROM hookd.users WHERE user_id = %s"
            cur.execute(sql, (user_id,))
            row = cur.fetchone()
            if row:
                return {"success": True, "data": row[0]}
            else:
                return {"success": False, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_email_by_username(username):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT email FROM hookd.users WHERE username = %s"
            cur.execute(sql, (username,))
            row = cur.fetchone()
            if row:
                return {"success": True, "data": row[0]}
            else:
                return {"success": False, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_username_by_user_id(user_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT username FROM hookd.users WHERE user_id = %s"
            cur.execute(sql, (user_id,))
            row = cur.fetchone()
            if row:
                return {"success": True, "data": row[0]}
            else:
                return {"success": False, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_username_by_email(email):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT username FROM hookd.users WHERE email = %s"
            cur.execute(sql, (email,))
            row = cur.fetchone()
            if row:
                return {"success": True, "data": row[0]}
            else:
                return {"success": False, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def update_username(user_id, username):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "UPDATE hookd.users SET username = %s WHERE user_id = %s"
            cur.execute(sql, (username, user_id))
            conn.commit()
            if cur.rowcount == 0:
                return {"success": False, "error": "User not found"}
            return {"success": True}
    except psycopg2.IntegrityError as err:
        conn.rollback()
        if err.pgcode == "23505":
            return {"success": False, "error": "Username already in use"}
        return {"success": False, "error": f"Something went wrong: {err}"}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def update_image(user_id, image):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "UPDATE hookd.users SET image = %s WHERE user_id = %s"
            cur.execute(sql, (image, user_id))
            conn.commit()
            if cur.rowcount == 0:
                return {"success": False, "error": "User not found"}
            return {"success": True}
    except psycopg2.IntegrityError as err:
        conn.rollback()
        if err.pgcode == "23505":
            return {"success": False, "error": "Username already in use"}
        return {"success": False, "error": f"Something went wrong: {err}"}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def delete_user(user_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "DELETE FROM hookd.users WHERE user_id = %s"
            cur.execute(sql, (user_id,))
            conn.commit()
            if cur.rowcount == 0:
                return {"success": False, "error": "User not found"}
            return {"success": True}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)

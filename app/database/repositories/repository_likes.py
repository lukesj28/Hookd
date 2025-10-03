import psycopg2

from app.database.db import get_conn, put_conn


def create_like(liker, post):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO hookd.likes (liker, post) VALUES (%s, %s)"
            cur.execute(sql, (liker, post))
            conn.commit()
            return {"success": True}
    except psycopg2.IntegrityError as err:
        conn.rollback()
        if err.pgcode == "23505":
            return {"success": False, "error": "Already liked"}
        return {"success": False, "error": f"Something went wrong: {err}"}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_like_count(post_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT COUNT(*) FROM hookd.likes WHERE post_id = %s"
            cur.execute(sql, (post_id,))
            return {"success": True, "data": cur.fetchone()[0]}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def delete_like(liker, post_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "DELETE FROM hookd.likes WHERE liker = %s AND post_id = %s"
            cur.execute(sql, (liker, post_id))
            conn.commit()
            if cur.rowcount == 0:
                return {"success": False, "error": "Like not found"}
            return {"success": True}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)

import psycopg2
from datetime import datetime

from app.database.db import get_conn, put_conn


def create_post(poster, image, description, pattern):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO hookd.posts (poster, image, description, pattern) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, (poster, image, description, pattern))
            conn.commit()
            return {"success": True}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_posts(poster):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT image, datetime FROM hookd.posts WHERE poster = %s"
            cur.execute(sql, (poster,))
            rows = cur.fetchall()
            if rows:
                return {"success": True, "data": [{"image": r[0], "datetime": r[1]} for r in rows]}
            else:
                return {"success": False, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_post(post_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT poster, image, datetime, description, pattern FROM hookd.posts WHERE post_id = %s"
            cur.execute(sql, (post_id,))
            row = cur.fetchone()
            if row:
                data = {"poster": row[0],
                        "image": row[1],
                        "datetime": row[2],
                        "description": row[3],
                        "pattern": row[4]}
                return {"success": True, "data": data}
            else:
                return {"success": False, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def update_image(post_id, image):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "UPDATE hookd.posts SET image = %s, edited = %s WHERE post_id = %s"
            now = datetime.now()
            cur.execute(sql, (image, now, post_id))
            conn.commit()
            if cur.rowcount == 0:
                return {"success": False, "error": "Post not found"}
            return {"success": True}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def update_description(post_id, description):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "UPDATE hookd.posts SET description = %s, edited = %s WHERE post_id = %s"
            now = datetime.now()
            cur.execute(sql, (description, now, post_id))
            conn.commit()
            if cur.rowcount == 0:
                return {"success": False, "error": "Post not found"}
            return {"success": True}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def update_pattern(post_id, pattern):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "UPDATE hookd.posts SET pattern = %s, edited = %s WHERE post_id = %s"
            now = datetime.now()
            cur.execute(sql, (pattern, now, post_id))
            conn.commit()
            if cur.rowcount == 0:
                return {"success": False, "error": "Post not found"}
            return {"success": True}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def delete_post(post_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "DELETE FROM hookd.posts WHERE post_id = %s"
            cur.execute(sql, (post_id,))
            conn.commit()
            if cur.rowcount == 0:
                return {"success": False, "error": "Post not found"}
            return {"success": True}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)

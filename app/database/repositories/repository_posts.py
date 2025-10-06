import psycopg2
from psycopg2.extras import Json
from datetime import datetime

from app.database.db import get_conn, put_conn


def create_post(poster_id, image, description, pattern):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO hookd.posts (poster_id, image, description, pattern) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, (poster_id, image, description, Json(pattern)))
            conn.commit()
            return {"success": True}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_posts(poster_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT post_id, image, datetime, edited FROM hookd.posts WHERE poster_id = %s"
            cur.execute(sql, (poster_id,))
            rows = cur.fetchall()
            if rows:
                return {"success": True, "data": [{
                    "post_id": r[0],
                    "image": r[1],
                    "datetime": f"{r[2].strftime("%b %d, %Y")}(edited)" if r[3] else f"{r[2].strftime("%b %d, %Y")}"} for r in rows]
                }
            return {"success": True, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_post(post_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT poster_id, image, datetime, description, pattern, edited FROM hookd.posts WHERE post_id = %s"
            cur.execute(sql, (post_id,))
            row = cur.fetchone()
            if row:
                data = {"poster_id": row[0],
                        "image": row[1],
                        "datetime": f"{row[2].strftime("%b %d, %Y - %H:%M")}(edited)" if row[5] else f"{row[2].strftime("%b %d, %Y - %H:%M")}",
                        "description": row[3],
                        "pattern": row[4]}
                return {"success": True, "data": data}
            return {"success": False, "error": "Post not found"}
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
            cur.execute(sql, (Json(pattern), now, post_id))
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

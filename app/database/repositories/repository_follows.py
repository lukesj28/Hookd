import psycopg2

from app.database.db import get_conn, put_conn


def create_follow(follower_id, followed_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO hookd.follows (follower, followed) VALUES (%s, %s)"
            cur.execute(sql, (follower_id, followed_id))
            conn.commit()
            return {"success": True}
    except psycopg2.IntegrityError as err:
        conn.rollback()
        if err.pgcode == "23505":
            return {"success": False, "error": "Already following"}
        elif err.pgcode == "23514":
            return {"success": False, "error": "Cannot follow yourself"}
        return {"success": False, "error": f"Something went wrong: {err}"}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_followers(user_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT follower FROM hookd.follows WHERE followed = %s"
            cur.execute(sql, (user_id,))
            rows = cur.fetchall()
            data = [r[0] for r in rows]
            if rows:
                return {"success": True, "data": data}
            return {"success": True, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_following(user_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT followed FROM hookd.follows WHERE follower = %s"
            cur.execute(sql, (user_id,))
            rows = cur.fetchall()
            data = [r[0] for r in rows]
            if rows:
                return {"success": True, "data": data}
            return {"success": True, "data": None}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_follower_count(user_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT COUNT(*) FROM hookd.follows WHERE followed = %s"
            cur.execute(sql, (user_id,))
            return {"success": True, "data": cur.fetchone()[0]}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def read_following_count(user_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "SELECT COUNT(*) FROM hookd.follows WHERE follower = %s"
            cur.execute(sql, (user_id,))
            return {"success": True, "data": cur.fetchone()[0]}
    except psycopg2.Error as err:
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)


def delete_follow(follower_id, followed_id):
    conn = get_conn()

    try:
        with conn.cursor() as cur:
            sql = "DELETE FROM hookd.follows WHERE follower = %s AND followed = %s"
            cur.execute(sql, (follower_id, followed_id))
            conn.commit()
            if cur.rowcount == 0:
                return {"success": False, "error": "Relationship not found"}
            return {"success": True}
    except psycopg2.Error as err:
        conn.rollback()
        return {"success": False, "error": f"Something went wrong: {err}"}
    finally:
        put_conn(conn)

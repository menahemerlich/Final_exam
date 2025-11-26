
def inlay_strategy(conn):
    cur = conn.cursor()
    cur.execute("""
                UPDATE soldiers SET status = 'טופל' WHERE id IN (SELECT id FROM soldiers ORDER BY `Distance`DESC LIMIT 160)
                """)
    conn.commit()
    cur.execute("""
                    UPDATE soldiers SET house_id = 2 WHERE id IN (SELECT id FROM soldiers ORDER BY `Distance` DESC LIMIT 160)
                    """)
    conn.commit()
    cur.execute("""
                    UPDATE soldiers SET house_id = 1 WHERE id IN (SELECT id FROM soldiers ORDER BY `Distance` DESC LIMIT 80)
                    """)
    conn.commit()
    cur.execute("""
                            UPDATE soldiers SET room_id = 10 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 80)
                            """)
    conn.commit()
    cur.execute("""
                            UPDATE soldiers SET room_id = 9 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 72)
                            """)
    conn.commit()
    cur.execute("""
                    UPDATE soldiers SET room_id = 8 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 64)
                    """)
    conn.commit()
    cur.execute("""
                        UPDATE soldiers SET room_id = 7 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 56)
                        """)
    conn.commit()
    cur.execute("""
                        UPDATE soldiers SET room_id = 6 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 48)
                        """)
    conn.commit()
    cur.execute("""
                        UPDATE soldiers SET room_id = 5 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 40)
                        """)
    conn.commit()
    cur.execute("""
                        UPDATE soldiers SET room_id = 4 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 32)
                        """)
    conn.commit()
    cur.execute("""
                        UPDATE soldiers SET room_id = 3 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 24)
                        """)
    conn.commit()
    cur.execute("""
                        UPDATE soldiers SET room_id = 2 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 16)
                        """)
    conn.commit()
    cur.execute("""
                        UPDATE soldiers SET room_id = 1 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 1 LIMIT 8)
                        """)
    conn.commit()
    cur.execute("""
                                UPDATE soldiers SET room_id = 10 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 80)
                                """)
    conn.commit()
    cur.execute("""
                                UPDATE soldiers SET room_id = 9 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 72)
                                """)
    conn.commit()
    cur.execute("""
                        UPDATE soldiers SET room_id = 8 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 64)
                        """)
    conn.commit()
    cur.execute("""
                            UPDATE soldiers SET room_id = 7 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 56)
                            """)
    conn.commit()
    cur.execute("""
                            UPDATE soldiers SET room_id = 6 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 48)
                            """)
    conn.commit()
    cur.execute("""
                            UPDATE soldiers SET room_id = 5 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 40)
                            """)
    conn.commit()
    cur.execute("""
                            UPDATE soldiers SET room_id = 4 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 32)
                            """)
    conn.commit()
    cur.execute("""
                            UPDATE soldiers SET room_id = 3 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 24)
                            """)
    conn.commit()
    cur.execute("""
                            UPDATE soldiers SET room_id = 2 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 16)
                            """)
    conn.commit()
    cur.execute("""
                            UPDATE soldiers SET room_id = 1 WHERE id IN (SELECT id FROM soldiers WHERE house_id = 2 LIMIT 8)
                            """)
    conn.commit()







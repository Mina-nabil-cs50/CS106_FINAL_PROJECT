from Database.db_manager import get_connection

def load_payment_by_id(payment_id):
    """
    conn = get_connection()  # Ensure get_connection is defined or imported
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Query the payment record
    cursor.execute('SELECT * FROM payments WHERE payment_id = ?', (payment_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        print("Payment loaded from database:")
        print(f"Payment ID: {row[0]}")
        print(f"Room ID: {row[1]}")
        print(f"Amount: {row[2]}")
        return row
    else:
        print("Payment Not found")

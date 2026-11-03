def get_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"id": row[0], "name": row[1], "email": row[2], "age": row[3]})

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE students SET name = ?, email = ?, age = ? WHERE id = ?',
        (data['name'], data['email'], data.get('age', 0), student_id)
    )
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Student not found"}), 404
    conn.close()
    return jsonify({"message": "Student updated"})

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Student not found"}), 404
    conn.close()
    return jsonify({"message": "Student deleted"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

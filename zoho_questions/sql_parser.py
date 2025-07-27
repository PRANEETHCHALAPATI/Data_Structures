import re

def parse_sql(query):
    query = query.strip().strip(';')  # Clean input
    
    result = {}
    
    # Match operation
    op_match = re.match(r"(?i)^\s*(SELECT|INSERT|UPDATE|DELETE)", query)
    if op_match:
        result["operation"] = op_match.group(1).upper()

    # Extract table name
    table_match = re.search(r"(?i)\bFROM\s+([a-zA-Z_][\w]*)", query)
    if not table_match:
        table_match = re.search(r"(?i)\bINTO\s+([a-zA-Z_][\w]*)", query)
    if not table_match:
        table_match = re.search(r"(?i)\bUPDATE\s+([a-zA-Z_][\w]*)", query)
    if table_match:
        result["table"] = table_match.group(1)

    # Extract columns (SELECT only)
    select_cols = re.search(r"(?i)^SELECT\s+(.*?)\s+FROM", query)
    if select_cols:
        cols = [col.strip() for col in select_cols.group(1).split(',')]
        result["columns"] = cols

    # Extract WHERE clause
    where_match = re.search(r"(?i)\bWHERE\s+(.+)", query)
    if where_match:
        result["where"] = where_match.group(1)

    return result

# 🔍 Example Usage
queries = [
    "SELECT name, age FROM users WHERE age > 21;",
    "INSERT INTO orders (id, total) VALUES (1, 100);",
    "UPDATE employees SET salary = 50000 WHERE id = 3;",
    "DELETE FROM logs WHERE created_at < '2023-01-01';"
]

for q in queries:
    print(f"Query: {q}")
    print("Parsed:", parse_sql(q), end="\n\n")

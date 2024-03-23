from lark import Lark, Token

# Определение грамматики с игнорированием пробелов
grammar = """
    %import common.WS
    %ignore WS

    sql_statement       : create_statement | drop_statement
    create_statement   : "CREATE" "TABLE" table_name "(" column_definitions ")"
    drop_statement     : "DROP" "TABLE" table_name
    column_definitions : column_definition ("," column_definition)*
    column_definition  : column_name data_type
    table_name         : /[a-zA-Z_][a-zA-Z0-9_]*/
    column_name        : /[a-zA-Z_][a-zA-Z0-9_]*/
    data_type          : "INT" | "VARCHAR" "(" integer ")" | "BOOLEAN"
    integer            : /[0-9]+/
"""

# Создание парсера
parser = Lark(grammar, start='sql_statement')

# Функция для парсинга строки
def parse_sql(input_sql):
    return parser.parse(input_sql)

# Пример использования
if __name__ == "__main__":
    input_sql = "CREATE TABLE users (id INT, name VARCHAR(50), active BOOLEAN)"
    parsed_result = parse_sql(input_sql)
    print(parsed_result)

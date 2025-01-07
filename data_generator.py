def generate_inserts(tables, sample_data, output_file="insert_data.sql"):
    with open("migration/" + output_file, "w") as sql_file:
        for table, columns in tables.items():
            for data in sample_data[table]:
                filtered_columns = []
                values = []
                for column in columns:
                    if data[column] is not None:
                        filtered_columns.append(column)
                        if isinstance(data[column], str):
                            values.append(f"'{data[column]}'")
                        elif isinstance(data[column], int):
                            values.append(str(data[column]))

                column_list = ", ".join(filtered_columns)
                str_values = ", ".join(values)

                insert_statement = f"INSERT INTO {table} ({column_list}) VALUES ({str_values});"
                sql_file.write(insert_statement + "\n")

    print(f"Plik SQL został wygenerowany: {output_file}")

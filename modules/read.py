def read_data(connection, range, table_id):
    sheets = connection.spreadsheets()
    result = sheets.values().get(spreadsheetId = table_id, range = range).execute()
    return result['values']
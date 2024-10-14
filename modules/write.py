def write_data(connection, table_id, data, range):
    sheets = connection.spreadsheets()
    body = {
        "values": data
    }
    result = sheets.values().update(spreadsheetId = table_id, range = range, body = body, valueInputOption = 'RAW').execute()
    
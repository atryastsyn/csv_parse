import os
import csv

# iterate through files in /csv folder

PATH = 'csv/'
RESULT_FILE_NAME = 'result.txt'
DELIMITER = ';'
USER_ID_COLUMN_NAME = 'User ID'

user_ids = set()

print(80*'-')
with os.scandir(PATH) as entries:
    for entry in entries:
        if entry.is_file():
            try:
                with open(entry, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
                    print(f'Process with file {entry.name}')
                    row_count = 0
                    user_ids_count = 0
                    for row in csv_reader:
                        user_id = row[1].strip('\n ')
                        if user_id == USER_ID_COLUMN_NAME:
                            continue
                        row_count += 1
                        try:
                            user_id_int = int(user_id)
                            if user_id in user_ids:
                                print(f'User id {user_id} already added')
                                continue
                            user_ids.add(user_id)
                            user_ids_count += 1
                        except ValueError:
                            print(f'{user_id} can to be converted to int')
                    print(f'Found {user_ids_count} valid user_ids in {row_count} lines, {len(user_ids)} total')
                    print(80*'-')
            except Exception as e:
                print(f'Error occured while working with file {entry.name}: {e}')


with open(RESULT_FILE_NAME, 'w') as result_file:
    result_file.write(', '.join(user_ids))
    print(f'Result user_ids saved to {RESULT_FILE_NAME} - {len(user_ids)} unique user ids')


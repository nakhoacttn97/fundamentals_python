import xu_ly_tap_tin_csv

filename = input('Nhập tên tập tin:\n')
listContent = [['Johnny Lee', '0913 753852'], ['Peter Son', '0989 753951'], ['Johnnathan','0903 123456']]
xu_ly_tap_tin_csv.write_csv_file(filename, listContent)
xu_ly_tap_tin_csv.read_csv_file_column(filename)
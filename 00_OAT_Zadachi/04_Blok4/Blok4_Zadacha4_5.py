print('\n Задача БЛОК 4, Задачи 4.5.')

print('----------')

# Чеки

import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')

    checks = list(map(lambda x: sorted(x.split('\n')), text.split("---")))
    for i in checks:
        add = {}
        for j in i:
            if j == '':
                continue

            cc = j.split('\t')
            key, val = (cc[0], int(cc[1])), int(cc[2])

            if key in add:
                add[key] += val
            else:
                add[key] = val
        s1 = add.keys()
        s = []
        for i in s1:
            s.append([i[0], int(add[i]), int(i[1])])
        s.sort()
        f = {}
        for i in s:
            f[(i[0], i[2])] = add[(i[0], i[2])]
            del add[(i[0], i[2])]
        if f:
            worksheet = workbook.add_worksheet()
            for row, (item_price, count) in enumerate(f.items()):
                worksheet.write(row, 0, item_price[0])
                worksheet.write(row, 1, float(item_price[1]))
                worksheet.write(row, 2, float(count))
                worksheet.write(row, 3, f'=B{row + 1}*C{row + 1}')

            row += 1

            worksheet.write(row, 0, 'Итого')
            worksheet.write(row, 3, f'=SUM(D1:D{row})')
    workbook.close()


print('----------')

# Учебная ведомость

from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, name, *marks):
    d = DocxTemplate(name)
    marks = sorted(marks, key=lambda x: x[0])
    context = {'class_name': class_name,
               'subject_name': subject_name,
               'marks': [{'num': i + 1, 'fio': marks[i][0], 'mark': marks[i][1]}
                         for i in range(len(marks))]}
    d.render(context)
    d.save("res.docx")
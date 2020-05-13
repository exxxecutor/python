import tkinter
import tkinter.ttk as ttk
from get_xml import get_xml, VALUTE_NAME_BLOCK, VALUTE_VALUE_BLOCK
import matplotlib
import matplotlib.pyplot as plt

root = get_xml()
RUSSIAN_RUBLE = 'Российский рубль'

MONTH_NUM = (
    ('Январь', '01'),
    ('Февраль', '02'),
    ('Март', '03'),
    ('Апрель', '04'),
    ('Май', '05'),
    ('Июнь', '06'),
    ('Июль', '07'),
    ('Август', '08'),
    ('Сентябрь', '09'),
    ('Октябрь', '10'),
    ('Ноябрь', '11'),
    ('Декабрь', '12'),
)

MONTH_LEN = 30

YEARS = (
    '2019',
    '2020',
)


# handlers
def onclick_convert(first_valute_combobox, second_valute_combobox, to_convert, result_entry):
    def wrapper():
        # find corresponding valute value
        first_value = None
        second_value = None
        for valute in root:
            if valute.find(VALUTE_NAME_BLOCK).text == first_valute_combobox.get():
                first_value = float(valute.find(VALUTE_VALUE_BLOCK).text.replace(',', '.'))

            if valute.find(VALUTE_NAME_BLOCK).text == second_valute_combobox.get():
                second_value = float(valute.find(VALUTE_VALUE_BLOCK).text.replace(',', '.'))

        # special case
        if first_valute_combobox.get() == RUSSIAN_RUBLE:
            first_value = 1.0
        if second_valute_combobox.get() == RUSSIAN_RUBLE:
            second_value = 1.0

        try:
            to_convert_value = int(to_convert.get())
            result = to_convert_value * first_value / second_value
        except (ValueError, AssertionError):
            result = -1

        result_entry.configure(state='enabled')
        result_entry.delete(0, 'end')
        result_entry.insert(0, result if result != -1 else 'Некорректное значение. (int > 0 req.)')
        result_entry.configure(state='disabled')

    return wrapper


def onclick_graph(period_entry, valute_entry):
    def wrapper():
        # fill
        month_num = [month_item[1] for month_item in MONTH_NUM if month_item[0] == period_entry.get().split(' ')[0]][0]
        to_plot = ([], [])
        for i in range(0, MONTH_LEN + 1, 5):
            temp_root = get_xml('%02d/%s/%s' % (i, month_num, period_entry.get().split(' ')[1]))
            for valute in temp_root:
                if valute.find(VALUTE_NAME_BLOCK).text == valute_entry.get():
                    to_plot[0].append(i)
                    to_plot[1].append(float(valute.find(VALUTE_VALUE_BLOCK).text.replace(',', '.')))
        # end fill

        matplotlib.use('TkAgg')
        fig = plt.figure()
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab2)
        plot_widget = canvas.get_tk_widget()
        plt.plot(to_plot[0], to_plot[1])
        plt.grid()
        plot_widget.grid(row=4, column=3)

    return wrapper


window = tkinter.Tk()
window.title('Test')
window.geometry('900x600')

tabs = ttk.Notebook(window)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)

# fill tab1
label1 = ttk.Label(tab1, text='Конвертировать из:')
valutes_box1 = ttk.Combobox(tab1)
label2 = ttk.Label(tab1, text='в')
valutes_box2 = ttk.Combobox(tab1)
label3 = ttk.Label(tab1, text='Сколько конвертировать:')
to_convert = ttk.Entry(tab1, width=20)
label4 = ttk.Label(tab1, text='Результат:')
result = ttk.Entry(tab1, width=20)
result.configure(state='disabled')  # readonly
convert_button = ttk.Button(tab1, text='Конвертировать', command=onclick_convert(valutes_box1,
                                                                                 valutes_box2,
                                                                                 to_convert,
                                                                                 result))

# fill boxes with valutes names
for valutes_box in [valutes_box1, valutes_box2]:
    valutes_box['values'] = [RUSSIAN_RUBLE] + [node.text for node in root.iter(VALUTE_NAME_BLOCK)]

# place them in the frame next to each other
# row 0
label1.grid(column=0, row=0)
valutes_box1.grid(column=1, row=0, padx=10)
label2.grid(column=2, row=0)
valutes_box2.grid(column=3, row=0, padx=10)
convert_button.grid(column=4, row=0)
# row 1
label3.grid(column=0, row=1)
to_convert.grid(column=1, row=1, pady=20)
label4.grid(column=2, row=1, padx=10)
result.grid(column=3, row=1)

tabs.add(tab1, text="Курсы валют")
tabs.add(tab2, text="График")

# fill tab2
period_label = ttk.Label(tab2, text='Период:')
period_entry = ttk.Combobox(tab2)
valute_label = ttk.Label(tab2, text='Валюта:')
valute_entry = ttk.Combobox(tab2)
graph_button = ttk.Button(tab2, text='График', command=onclick_graph(period_entry, valute_entry))

# fill valute_entry
valute_entry['values'] = [node.text for node in root.iter(VALUTE_NAME_BLOCK)]
period_entry['values'] = [month[0] + ' ' + year for year in YEARS for month in MONTH_NUM]

# place tab2
period_label.grid(column=0, row=0)
period_entry.grid(column=1, row=0)
valute_label.grid(column=0, row=1, pady=20)
valute_entry.grid(column=1, row=1)
graph_button.grid(column=0, row=2)

tabs.pack(expand=1, fill='both')
window.mainloop()

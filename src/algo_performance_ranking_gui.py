import tkhtmlview
import PySimpleGUI as sg


def set_html(widget, html, strip=True):
    # prev_state = widget.cget('state')
    # widget.config(state=sg.tk.NORMAL)
    # widget.delete('1.0', sg.tk.END)
    # widget.tag_delete(widget.tag_names)
    tkhtmlview.html_parser.HTMLTextParser().w_set_html(widget, html, strip=strip)
    # widget.config(state=prev_state)

def algo_perf_gui():
    with open(r'C:\Users\Thom van den Hil\Desktop\Modelling-B\src\out\intuitive_algo_2\11-Data assignment parcel transport 2 Small-2022-05-26-11-28-26\graph_11_Data assignment parcel transport 2 Small_2022_05_26_11_28_26.html', 'r') as file:
        graph_html = file.read()

    left_column = [
        [sg.Text('DATA SET DATA')]
    ]
    right_column = [
        [sg.Multiline(
            size=(25, 10),
            border_width=2,
            disabled=True,
            no_scrollbar=True,
            expand_x=True,
            expand_y=True,
            key='graph')],
    ]
    layout = [
        [
            sg.Column(left_column),
            sg.VSeperator(),
            sg.Column(right_column),
        ]
    ]

    window = sg.Window('Algorithms Performance Ranking', layout, finalize=True, use_default_focus=False)
    right_column_widget = window['graph'].Widget
    set_html(right_column_widget, graph_html)

    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

    return window.close()



def main() -> None:
    algo_perf_gui()


if __name__ == '__main__':
    main()
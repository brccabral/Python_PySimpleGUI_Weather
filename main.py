import PySimpleGUI as sg

image_col = sg.Column([[sg.Image("", key="-IMAGE-", background_color="white")]])
info_col = sg.Column(
    [
        [
            sg.Text(
                "",
                key="-LOCATION-",
                font="Calibri 30",
                background_color="red",
                pad=0,
                visible=False,
            )
        ],
        [
            sg.Text(
                "",
                key="-TIME-",
                font="Calibri 16",
                background_color="black",
                text_color="white",
                pad=0,
                visible=False,
            )
        ],
        [
            sg.Text(
                "",
                key="-TEMP-",
                font="Calibri 16",
                justification="center",
                expand_x=False,
                pad=(0, 10),
                visible=False,
                background_color="white",
                text_color="black",
            ),
        ],
    ]
)

layout = [
    [sg.Input(key="-INPUT-", expand_x=True), sg.Button("Enter", key="-ENTER-")],
    [image_col, info_col],
]

window = sg.Window("Wheather", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-ENTER-":
        window["-LOCATION-"].update("test", visible=True)
        window["-TIME-"].update("test", visible=True)
        window["-TEMP-"].update("test", visible=True)
        window["-IMAGE-"].update("symbols/snow.png", visible=True)

window.close()

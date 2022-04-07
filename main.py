import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"


def get_weather_data(location: str):
    url = f"https://www.google.com/search?q=weather+{location.replace(' ', '%20')}"
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    html = session.get(url)

    soup = bs(html.text, "html.parser")
    name = soup.find("div", attrs={"id": "wob_loc"}).text
    time = soup.find("div", attrs={"id": "wob_dts"}).text
    weather = soup.find("span", attrs={"id": "wob_dc"}).text
    temp = soup.find("span", attrs={"id": "wob_tm"}).text

    return name, time, weather, temp


sg.theme("reddit")
image_col = sg.Column([[sg.Image("", key="-IMAGE-", background_color="white")]])
info_col = sg.Column(
    [
        [
            sg.Text(
                "",
                key="-LOCATION-",
                font="Calibri 30",
                background_color="red",
                text_color="white",
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
    [
        sg.Input(key="-INPUT-", expand_x=True),
        sg.Button("Enter", key="-ENTER-", button_color="black", border_width=0),
    ],
    [image_col, info_col],
]

window = sg.Window("Weather", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-ENTER-":
        name, time, weather, temp = get_weather_data(values["-INPUT-"])
        window["-LOCATION-"].update(name, visible=True)
        window["-TIME-"].update(time.split(" ")[0], visible=True)
        window["-TEMP-"].update(f"{temp} \u2103 ({weather})", visible=True)
        window["-IMAGE-"].update("symbols/snow.png", visible=True)

window.close()

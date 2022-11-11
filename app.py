import PySimpleGUI as sg
import qrcode

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer

# ウィンドウの内容を定義する
layout = [[sg.Text('URL:'),sg.InputText(key='-URL-')],
          [sg.Radio('SquareModuleDrawer', group_id='ModuleSelect', default=True, key='-SquareModuleDrawer-'),
           sg.Radio('GappedSquareModuleDrawer', group_id='ModuleSelect', key='-GappedSquareModuleDrawer-'),
           sg.Radio('CircleModuleDrawer', group_id='ModuleSelect', key='-CircleModuleDrawer-')],
         [sg.Radio('RoundedModuleDrawer', group_id='ModuleSelect', key='-RoundedModuleDrawer-'),
           sg.Radio('VerticalBareDrawer', group_id='ModuleSelect', key='-VerticalBarsDrawer-'),
           sg.Radio('HorizontalBarsDrawer', group_id='ModuleSelect', key='-HorizontalBarsDrawer-')],
          [sg.Button('QRコード生成', key='-CREATE_QR_CODE-')],
          [sg.Image(key='-QR_CODE_IMG-')]]

# ウィンドウを作成
window = sg.Window('QRコード生成アプリ', layout=layout, size=(550, 600))

while True:
    event, values = window.read()
    if event == '-CREATE_QR_CODE-':
        
        def add(module):
            qr = qrcode.QRCode(
                version = 5,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size = 10,
                border = 2,
            )
            qr.add_data(values['-URL-'])
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=module())
            img.save("QRcode.png")
            window['-QR_CODE_IMG-'].update('./QRcode.png')

        if values["-SquareModuleDrawer-"]:
            add(SquareModuleDrawer)
        
        if values["-GappedSquareModuleDrawer-"]:
            add(GappedSquareModuleDrawer)
            
        if values["-CircleModuleDrawer-"]:
            add(CircleModuleDrawer)
            
        if values["-RoundedModuleDrawer-"]:
            add(RoundedModuleDrawer)
            
        if values["-VerticalBarsDrawer-"]:
            add(VerticalBarsDrawer)

        if values["-HorizontalBarsDrawer-"]:
            add(HorizontalBarsDrawer)

    if event == sg.WIN_CLOSED:
        break
    

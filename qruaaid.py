
# author: MiguelHeCa
# date: 2022-02-28

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def main():
    links = {}
    links['UNfund'] = ["https://crisisrelief.un.org/t/ukraine",
            'un-logo.png',
            (0, 0, 0),
            (0, 0, 255)]
    links['UABank'] = ["https://bank.gov.ua/en/about/support-the-armed-forces",
            'ua-logo.png',
            (238, 177, 17),
            (0, 0, 255)]


    for k,v in links.items():
        qr = qrcode.QRCode(version=5,
                box_size=10,
                border=5,
                error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(v[0])
        qr.make(fit=True)

        img = qr.make_image(
                image_factory=StyledPilImage, color_mask=RadialGradiantColorMask(
                center_color=v[2],
                edge_color=v[3]),
                embeded_image_path=v[1],
                module_drawer=RoundedModuleDrawer()
                )
        img.save(f'qrcode{k}.png')


if __name__=='__main__':
    main()



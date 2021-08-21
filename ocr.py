from PIL import Image
import pytesseract

#! tesseract installation is required, make sure the path is where you installed tesseract at!
# Installation guide at https://stackoverflow.com/a/53672281
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def imageToText(file_path):
    import sharedData
    text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim+eng')  ## chi_sim for Chinese simplified language pack
    # main.textInfo = main.textInfo + text
    sharedData.ocrResult = file_path

    # print(main.textInfo)
    # main.root.event_generate("<<NewText>>", "123")
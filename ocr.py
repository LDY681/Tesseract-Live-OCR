from PIL import Image
import pytesseract
import sharedData
import difflib

#! tesseract installation is required, make sure the path is where you installed tesseract at!
# Installation guide at https://stackoverflow.com/a/53672281
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def imageToText(file_path):
    text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')  ## chi_sim for Chinese simplified language pack
    trimmedStrs = [line.strip() for line in text.splitlines() if line.strip()]
    insertNewLines(trimmedStrs)

def insertNewLines(trimmedStrs):
    lastOcrResult = sharedData.lastOcrResult
    # print("last OcrResult")
    # print(lastOcrResult)

    # print("new OcrResult")
    # print(trimmedStrs)

    for idxA, strA in enumerate(trimmedStrs):
        matched = False
        for idxB, strB in enumerate(lastOcrResult):
            if difflib.SequenceMatcher(None, strA, strB).ratio() > 0.8:
                # print(strA, ' matches ', strB, ' at index: ', idxB , '. Abort')
                matched = True
                break
            else:
                continue
        if matched == False:
            # print("no match found for ", strA, " add to array")
            sharedData.ocrResult.append(strA)
    print("final OcrResult")
    print(sharedData.ocrResult)
    sharedData.lastOcrResult = trimmedStrs
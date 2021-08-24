############## SDT OCR Functionality ###############
#
# Author: Dayu Liu
# Date: 8/12/21
# Description: OCR functionality
# Step 1: Scan a local image to generate new OCR result, delete the image after it's scanned
# Step 2: Compare latest OCR result with the new one, get rid of the duplicates and only insert new stuff to the final result
#

from PIL import Image
import pytesseract
import sharedData
import difflib
import os

#! tesseract installation is required, make sure the path is where you installed tesseract at!
# Installation guide at https://stackoverflow.com/a/53672281
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def imageToText(file_path):
    text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')  ## chi_sim for Chinese simplified language pack
    real_path = os.path.join(os.getcwd(), file_path) # get the absolute path of image so we can call os.remove to remove it
    os.remove(real_path) # delete this image
    trimmedStrs = [line.strip() for line in text.splitlines() if line.strip()]
    insertNewLines(trimmedStrs)

def insertNewLines(trimmedStrs):
    lastOcrResult = sharedData.lastOcrResult

    for idxA, strA in enumerate(trimmedStrs):
        matched = False
        for idxB, strB in enumerate(lastOcrResult):
            if difflib.SequenceMatcher(None, strA, strB).ratio() > 0.8:
                matched = True
                break
            else:
                continue
        if matched == False:
            sharedData.ocrResult.append(strA)
    print(sharedData.ocrResult)
    sharedData.lastOcrResult = trimmedStrs
import logging
import os
import fitz

logger = logging.getLogger('image_snatch')
logger.setLevel(logging.DEBUG)

OUTDIR = os.path.join(os.getcwd(),
                      "out")

def _checkfs(**kwargs):
    if not os.path.isfile(kwargs['pdf_path']):
        print("%s Not found!" % (pdf_path))
        exit(0)
    if not os.path.isdir(OUTDIR):
        print("%s Not found!" % (OUTDIR))
        exit(0)


def toPNG(pdf_path):
    _checkfs(pdf_path=pdf_path)
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix  = fitz.Pixmap(doc, xref)
            if pix.n - pix.alpha < 4:  # this is GRAY or RGB
                pix.writePNG("%s/p%s-%s.png" % (OUTDIR, i, xref))
                pix = None
            else:  # CMYK, convert to RGB first
                rgb = fitz.Pixmap(fitz.csRGB, pix)
                rgb.writePNG("out/p%s-%s.png" % (i, xref))
                rgb = None


def toJPEG(pdf_path):
    _checkfs(pdf_path=pdf_path)
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            print(repr(img))
            xref = img[0]
            pix  = fitz.Pixmap(doc, xref)
            if pix.n - pix.alpha < 4:  # this is GRAY or RGB
                pix.pillowWrite("%s/p%s-%s.jpeg" % (OUTDIR, i, xref),
                                optimize=True, dpi=(150, 150))
                pix = None
            else:  # CMYK, convert to RGB first
                rgb = fitz.Pixmap(fitz.csRGB, pix)
                rgb.pillowWrite("%s/p%s-%s.jpeg" % (OUTDIR, i, xref),
                                optimize=True, dpi=(150, 150))
                rgb = None


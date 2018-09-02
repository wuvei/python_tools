# -*- coding: UTF-8 -*-
import glob
import fitz
import os

outputPath = "./pic2PDF"
inputPath = "./input/"

def makedir(path):
    folder = os.path.exists(path)
    if not folder:                  #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("---  new folder...  ---")
		print("---  OK  ---")
    else:
        print("---  The folder already exists!  ---")

def pic2pdf():
    doc = fitz.open()
    #for img in sorted(glob.glob(inputPath+"/*")):  # 读取图片，确保按文件名排序
    for i in range(1, 19):
        img = glob.glob(inputPath+str(i)+".png")
        print(img)
        imgdoc = fitz.open(img[0])                 # 打开图片
        pdfbytes = imgdoc.convertToPDF()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                  # 将当前页插入文档
    makedir(outputPath)
    if os.path.exists(outputPath+"/allimages.pdf"):
        os.remove(outputPath+"/allimages.pdf")
    doc.save(outputPath+"/allimages.pdf")                 # 保存pdf文件

if __name__ == '__main__':
    pic2pdf()
    # for i in range(1,19):
    #     img = glob(inputPath+str(i)+".png")
    #     print(img)
import cv2
import numpy as np
import matplotlib.pyplot as plt

doll = cv2.imread('doll.png')
dress = cv2.imread('dress.png')
top = cv2.imread('top.png')
highRise = cv2.imread('highrise.png')
top2 = cv2.imread('top2.png')
jacket = cv2.imread('jacket.png')
shoes = cv2.imread('shoes.png')

def get_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Clicked at: x={x}, y={y}')

cv2.imshow('Doll', doll)
cv2.imshow('Dress', dress)
cv2.imshow('Top', top)
#cv2.imshow('Top2', top2)
#cv2.imshow('HighRise', highRise)
#cv2.imshow('Jacket', jacket)
#cv2.imshow('Shoes', shoes)

cv2.moveWindow('Doll', 0, 0)
cv2.moveWindow('Top', top.shape[1] + 20, 0)

cv2.setMouseCallback('Doll', get_click)
cv2.setMouseCallback('Top', get_click)
cv2.waitKey(0)
cv2.destroyAllWindows()
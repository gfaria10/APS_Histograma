import cv2
from matplotlib import pyplot as plt
import numpy as np

# fazendo a leitura da imagem
img = cv2.imread('./colorida.jpg')

# pixels de largura
print("Largura: {} pixels".format(img.shape[1]))
# pixels de altura
print("Altura: {} pixels".format(img.shape[0]))

# abre e apresenta a imagem na tela / também é possível mostrar de acordo com o RGB
cv2.imshow("imagem original", img)

# aguarda o usuario sair da imagem clicando em algo
cv2.waitKey()

# histograma
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(histr) 
plt.show()
cv2.waitKey()

# equalizando a imagem
img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
 
cv2.imwrite('result.jpg',hist_equalization_result)

cv2.imshow("imagem equalizada", hist_equalization_result)

cv2.waitKey()
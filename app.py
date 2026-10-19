from flask import Flask, Response
import cv2

app = Flask(__name__)

def fitGarment(doll, dollx, doll2x, dolly, garmentRightx, garmentLeftx, garmenty, garmentPath):
    garment = cv2.imread(garmentPath, cv2.IMREAD_UNCHANGED)

    dollDist = doll2x-dollx
    garmentDist = garmentLeftx - garmentRightx;
    resize = dollDist / garmentDist 

    garment = cv2.resize(garment, None,fx=resize, fy=resize, interpolation=cv2.INTER_AREA)
#ratio of the distances eg. should-to-should of doll and top
    cornerx = dollx - (round(garmentRightx * resize))
    cornery = dolly - (round(garmenty * resize))

    garment_bgr = garment[:, :, :3]
    alpha = garment[:, :, 3] / 255.0

    h, w = garment_bgr.shape[:2]
    roi = doll[cornery:cornery+h, cornerx:cornerx+w]

    for c in range(3):
        roi[:, :, c] = (alpha * garment_bgr[:, :, c] + (1 - alpha) * roi[:, :, c])

    doll[cornery:cornery+h, cornerx:cornerx+w] = roi    

    return doll

garmentConfiguration = {
    'topShoulder' : {'dollRightx' : 183 , 'dollLeftx' : 239 , 'dolly' : 98, }, #shoulder
    'topBust': {'dollRightx' : 175 , 'dollLeftx' : 245 , 'dolly' : 149 }, #bust
    'lowrise': {'dollRightx' : 169 , 'dollLeftx' : 249 , 'dolly' : 219 }, #hip
    'highrise': {'dollRightx' : 179 , 'dollLeftx' : 240 , 'dolly' : 198 }, #waist-ish
    'jacket' : {'dollRightx' : 199 , 'dollLeftx' : 220, 'dolly': 85}, #neck, oversized jacket
    'calfHighShoes' : {'dollRightx' : 176, 'dollLeftx': 242, 'dolly': 429} #calf/ knee high boots
}

garmentLibrary ={
    'dress.png' : {'category' : 'topShoulder', 'rightx' : 153, 'leftx' : 264, 'y' : 103,},
    'top.png' : {'category' : 'topShoulder', 'rightx' : 40, 'leftx' : 130, 'y' : 44,},
    'babydollTop.png' : {'category' : 'topBust', 'rightx' : 145, 'leftx' : 281, 'y' : 161,},
    'highrise.png' : {'category' : 'highrise', 'rightx' : 62, 'leftx' : 182, 'y' : 22,},
    'jacket.png' : {'category' : 'jacket', 'rightx' : 128, 'leftx' : 161, 'y' : 1,},
    'shoes.png' : {'category' : 'calfHighShoes', 'rightx' : 19, 'leftx' : 133, 'y' : 58,}

}

def fitGarmentByCategory (doll, category, garmentRightx, garmentLeftx, garmenty, garmentPath):
    anchors = garmentConfiguration[category]
    return fitGarment(doll, anchors['dollRightx'], anchors['dollLeftx'], anchors['dolly'], garmentRightx, garmentLeftx, garmenty, garmentPath)

def wearGarment(doll, filename):
    info = garmentLibrary[filename]
    return fitGarmentByCategory(doll, info['category'], info['rightx'], info['leftx'], info['y'], filename)

@app.route('/')
def home():
    doll = cv2.imread('doll.png')
    doll = wearGarment(doll, 'top.png')
    doll = wearGarment(doll, 'shoes.png')
    
    success, buffer = cv2.imencode('.png', doll)
    return Response(buffer.tobytes(), mimetype = 'image/png')

if __name__ == '__main__':
    app.run(debug = True)
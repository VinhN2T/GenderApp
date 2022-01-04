import numpy as np
import dlib
import cv2
import pickle

'''
   Giới tính 
'''
face_detector = dlib.get_frontal_face_detector()
xmean = pickle.load(open('./model/mean_X-preprocess.pickle','rb'))
svm_model = pickle.load(open('./model/svmModel_SVC.pickle','rb'))
pca_model = pickle.load(open('./model/pca_50.pickle','rb'))
haar= cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')

gender =['male','female']
# Ngưỡng threshold
thresh = 0.53
def gender_predict(filename):
    global gender,thresh
    img = cv2.imread('./static/images/upload/{}'.format(filename))
    face_detections = face_detector(img,1)
    
    # Gray
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # detect face 
    faces = haar.detectMultiScale(gray,1.3,5)
    
    for face in face_detections:
        l,t,r,b = face.left(),face.top(),face.right(),face.bottom()
        cv2.rectangle(img,(l,t),(r,b),(0,102,255),2)
    
    for (x,y,w,h) in faces:
        # resize roi về (100,100)
        roi = gray[y:y+h,x:x+w]
        roi = roi/255.0
        size = roi.shape[0]
        if size>100:
            roi_resize = cv2.resize(roi,(100,100),cv2.INTER_AREA)
        else:
            roi_resize = cv2.resize(roi,(100,100),cv2.INTER_CUBIC)
        # reshape(1,-1) -> flatten
        roi_reshape = roi_resize.reshape(1,-1)

        # PCA
        # Trừ cho xmean
        roi_mean= roi_reshape-xmean
        # giảm chiều bằng pca
        eigen_img = pca_model.transform(roi_mean)
        # predict bằng svm -> Nam hay nữ ? bao nhiêu phần trăm?
        result = svm_model.predict_proba(eigen_img)[0]
        predict = np.argmax(result)
        correct= result[predict]
        # Xử lý với ngưỡng thresh hold
        if (correct <= thresh) & (int(predict)==1):
            predict=0
            
        cv2.imwrite('./static/images/predict/{}'.format(filename),img)
        return (int(predict), round(correct,4))
    cv2.imwrite('./static/images/predict/{}'.format(filename),img)
    return -1, -1

#coding=gbk
from multiprocessing import Process, Queue, Pool, Manager, Lock
import numpy as np
import os, time, random, cv2
import camera_configs_540_120 as camera_configs

import pygame

# ��������
def broadcast(bc_recv):
    a = -1

    while True:
        try:
            a = bc_recv.get()
        except:
            pass

        if a > 10:		a = -1
        elif a >= 10:	a = 10
        elif a >= 9:	a = 9
        elif a >= 8:	a = 8
        elif a >= 7:	a = 7
        elif a >= 6:	a = 6
        elif a >= 5:	a = 5
        elif a >= 4.5:	a = 4.5
        elif a >= 4:	a = 4
        elif a >= 3.8:	a = 3.8
        elif a >= 3.6:	a = 3.6
        elif a >= 3.4:	a = 3.4
        elif a >= 3.2:	a = 3.2
        elif a >= 3:	a = 3
        elif a >= 2.8:	a = 2.8
        elif a >= 2.6:	a = 2.6
        elif a >= 2.4:	a = 2.4
        elif a >= 2.2:	a = 2.2
        elif a >= 2:	a = 2
        elif a >= 1.9:	a = 1.9
        elif a >= 1.8:	a = 1.8
        elif a >= 1.7:	a = 1.7
        elif a >= 1.6:	a = 1.6
        elif a >= 1.5:	a = 1.5
        elif a >= 1.4:	a = 1.4
        elif a >= 1.3:	a = 1.3
        elif a >= 1.2:	a = 1.2
        elif a >= 1.1:	a = 1.1
        elif a >= 1:	a = 1
        elif a >= 0.9:	a = 0.9
        elif a >= 0.8:	a = 0.8
        elif a >= 0.7:	a = 0.7
        elif a >= 0.6:	a = 0.6
        elif a >= 0.5:	a = 0.5
        elif a >= 0.4:	a = 0.4
        elif a >= 0.3:	a = 0.3
        elif a >= 0.2:	a = 0.2
        elif a >= 0.1:	a = 0.1
        elif a >= 0:	a = 0
        else:           a = -1

        if a == -1:
            continue

        mp3 = './' + repr(a) + 'm.mp3'

        pygame.mixer.init()
        track = pygame.mixer.music.load(mp3)
        pygame.mixer.music.play()
        time.sleep(1)
        pygame.mixer.music.stop()
        end = time.time()

class itemImg:
    def __init__(self):
        self.Left = np.empty(shape=[0, 2])
        self.Right = np.empty(shape=[0, 2])
        self.imgL = np.empty(shape=[0, 2])
        self.imgR = np.empty(shape=[0, 2])
        self.DeepData = np.empty(shape=[0, 2])

# CPUѹ������
class CP:
    pass

def CPUtest():
    i = 0
    while True:
        i = i + 1

# adding code-���˼��-�ж�Ŀ�꼰�Ӿ��δ� @NXT
# ������α���ȫ����������һ�������У���ȷ���þ���Ӧ�ñ�����
def is_inside(o, i):
    ox, oy, ow, oh = o
    ix, iy, iw, ih = i
    return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih

def draw_person(image, person):
    x, y, w, h = person
    # cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)

# ������ͷ����ʾ�Ĵ���:
def read_camera(queue_camera_bm, queue_camera_full,queue_camera_show):
    # ��������ͷ
    ##camera1 = cv2.VideoCapture(1)
    ##camera2 = cv2.VideoCapture(0)
    ##camera1.set(3, 640)  # ���÷ֱ���
    ##camera1.set(4, 360)
    ##camera2.set(3, 640)  # ���÷ֱ���
    ##camera2.set(4, 360)
    
    pickOneOfTwo = 0

    SwapCamera = not True    #��������ͷ
    key = cv2.waitKey(5)
    #end = time.clock()    #�������
    #start = time.clock()
    while True:
        pickOneOfTwo = pickOneOfTwo + 1
        if pickOneOfTwo  >= 2:
            pickOneOfTwo = 0
        #if not pickOneOfTwo:    #�������
        #    end = time.clock()
        #    delay_time =int((end-start) * 1000)#������ʱÿ��10֡ˢ��
        #    start = time.clock()
        #    print(delay_time)
        ret1 = 1
        ret2 = 1
        ##if SwapCamera:
        ##    ret1, Left = camera1.read()
        ##    ret2, Right = camera2.read()
        ##else:
        ##    ret1, Left = camera2.read()
        ##    ret2, Right = camera1.read()
        Left = cv2.imread('D:/Left_15.jpg')
        Right = cv2.imread('D:/Right_15.jpg')
        if pickOneOfTwo == 0:    #��ֵȡͼ��
            pass
        else:
            time.sleep(0.03)
            continue
        if ret1 and ret2:
            CutImg1 = Left[60:180, 50:590]  # y x
            CutImg2 = Right[60:180, 50:590]  # y x
            # cv2.imshow("left", CutImg1)
            # cv2.imshow("right", frame2)
            CutImg1 = cv2.cvtColor(CutImg1, cv2.COLOR_BGR2GRAY)
            CutImg2 = cv2.cvtColor(CutImg2, cv2.COLOR_BGR2GRAY)
            imgL = cv2.remap(CutImg1, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
            imgR = cv2.remap(CutImg2, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)
        else:
            time.sleep(0.01)
            continue

        cp = CP()    #to BM
        cp.imgL = imgL
        cp.imgR = imgR

        try:    #to BM
            clear = queue_camera_bm.get_nowait()
        except:
            pass
        queue_camera_bm.put(cp)

        try:    #to ObjectDetection
            clear = queue_camera_full.get_nowait()
        except:
            pass
        queue_camera_full.put(Left)

        try:    #to showimg
            clear = queue_camera_show.get_nowait()
        except:
            pass
        queue_camera_show.put(Left)

        #cv2.imshow("CutImg1", CutImg1)

        cv2.waitKey(5)
        #print(key)
        #if cv2.waitKey(3) & 0xFF == ord('q'):
        #    break
        #elif cv2.waitKey(2) & 0xFF == ord('s'):    #��������ͷ
        #    SwapCamera = not SwapCamera
        #    print(SwapCamera)
    

# ��ʾ ԭʼͼ�� ������Ϣ ��Ա��Ϣ
def showImg(queue_camera_show, bm_data, Object_data, bc_send):
    cv2.namedWindow("SHOW",cv2.WINDOW_NORMAL)
    #cv2.namedWindow("SHOW", 0);
    cv2.resizeWindow("SHOW", 1280, 720);
    cv2.moveWindow("SHOW",620,20);
    #Depth data processing parameters ������ݴ������
    DDPP = [
        [0,10,0,7,0],[3,17,4,11,7],[10,24,4,11,14],
        [17,31,4,11,21],[24,39,4,11,28],[31,42,4,11,35]
    ]    #Depth data processing array

    #BG = cv2.imread("/home/pi/Desktop/BirdVision/BG.bmp")#��ݮ��Ŀ¼
    BG = cv2.imread('./BG.jpg')#PCĿ¼
    zeroimg = np.zeros((360,640,3), dtype=np.uint8)
    DeepData  = np.zeros((42), dtype=np.uint16)
    show_img = zeroimg.copy()
    Deepimg = zeroimg.copy()
    personImg = zeroimg.copy()
    original_img = zeroimg.copy()
    objectImg = zeroimg.copy()

    # ������Ҫ��������ģ��ľ���
    distance = []
    single_distance = []
    cnt = 0

    while True:         
        original_sige = 0    #get person data
        try:
            original_img = queue_camera_show.get(1)
            original_sige = 1
        except:
            pass

        original_img = cv2.flip(src=original_img,flipCode=1)#������ת
        show_img = cv2.addWeighted(original_img, 1,objectImg, 1, 0) 
        cv2.imshow("SHOW", show_img)
        cv2.waitKey(10)


        Deep_sige = 0    #��Ӧ���� = DeepData[int((x-110)/10)]
        try:
            DeepData = bm_data.get_nowait()
            Deep_sige = 1
        except:
            pass

        person_sige = 0    #get person data
        try:
            found_filtered = Object_data.get_nowait()
            person_sige = 1
        except:
            pass
       
        if person_sige:    #����ʶ����
            personImg = BG.copy()    #���ͼ��
            #draw_person(personImg, (110,70,420,110))    #��ʾ�������
            for person in found_filtered:
                x1, y1, w1, h1 = person
                #draw_person(personImg,(int(x1+w1/4), int(y1+h1*2/15), int(w1/2), int(h1*11/15)))
                draw_person(personImg,(int(640-x1-w1*3/4), int(y1+h1*2/15), int(w1/2), int(h1*11/15)))#������ת
                #draw_person(personImg, person)
                #x1, y1, w1, h1 = person  # python ��������ô��ʾ��������Ǽ��С������ľ��ζ������꣬��û�������⵽�˵����꣩
         
        if Deep_sige:
            Deepimg = zeroimg.copy()    #���ͼ��
            #deepmax = Deepimg.min() + 200
            for i in range(6):
                Parameter = DDPP[i]
                #print(Parameter)
                cutData = DeepData[Parameter[0]:Parameter[1]]
                deepmin = cutData.min()
                if deepmin < 1400:
                    #print(deepmin)
                    cutData = cutData[Parameter[2]:Parameter[3]]
                    #print(cutData)
                    #print(cutData.tolist().index(deepmin))
                    tryResult = False
                    try:
                        aims = cutData.tolist().index(deepmin)
                        tryResult = True
                    except:
                        pass
                    if tryResult:
                        aims = aims+Parameter[4]
                        #print(aims)
                        #x_num = int(aims*10+80)
                        x_num = int(485 - aims*10)#�������� 640 - ԭ����
                        showmin = deepmin/100.
                        #print(showmin)
                        if showmin < 3:    #3���ں�ɫ
                            colorTest = (0, 0, 255)
                        elif showmin < 5:    #5������ɫ
                            colorTest = (0, 255, 0)
                        else:    #5��������ɫ
                            colorTest = (255, 255, 0)
                        cv2.putText(Deepimg, "%.1fM" % (showmin),(x_num, 350), cv2.FONT_HERSHEY_SIMPLEX, 1.0, colorTest, 3)

                        if showmin > 0:
                            single_distance.append(showmin)
                    #cv2.waitKey(0)
                #print(cutData)
        
        if len(single_distance):
            distance.append(min(single_distance))
        single_distance.clear()
        cnt = cnt + 1
        if cnt > 20:
            distance.sort()

            try:
                bc_send.put(distance[int(len(distance) / 2)])
            except:
                bc_send(0)
                pass

            distance.clear()
            cnt = 0

        if person_sige or Deep_sige:
            objectImg = cv2.addWeighted(personImg, 1, Deepimg, 1, 0)

def BM(queue_camera_bm, bm_data):
    num = 4
    blockSize = 10
    speckleWindowSize = 100
    # ˳����� �¼���� ��0��λ��
    # cut_data_array = np.zeros((462*4,3), dtype=np.int32)
    cut_data_array = np.zeros((924, 3), dtype=np.int16)
    ##cv2.namedWindow("cut img", 0);
    #cv2.resizeWindow("cut img", 420, 110);
    ##cv2.moveWindow("cut img",10,20);

    ##cv2.namedWindow("BM",0);
    ##cv2.moveWindow("BM",10,25+150);

    ##cv2.namedWindow("Sampled at intervals", 0);    #�������
    ##cv2.resizeWindow("Sampled at intervals", 420, 110);
    ##cv2.moveWindow("Sampled at intervals",55,25+150*2);

    ##cv2.namedWindow("Noise reduction", 0);    #����
    ##cv2.resizeWindow("Noise reduction", 420, 110);
    ##cv2.moveWindow("Noise reduction",55,25+150*3);

    ##cv2.namedWindow("Sort by distance", 0);    #��������
    ##cv2.resizeWindow("Sort by distance", 420, 110);
    ##cv2.moveWindow("Sort by distance",55,25+150*4);
    while True:
        try:
            cp = queue_camera_bm.get(1)
        except:
            continue
        imgL = cp.imgL
        imgR = cp.imgR
        stereo = cv2.StereoBM_create(64, 11)
        #stereo = cv2.StereoSGBM_create(0, 16 * num, blockSize, 0, 0, -10, 31, 20, speckleWindowSize, 32, 0)
        disparity = stereo.compute(imgL, imgR)
        disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        ##cv2.imshow("cut img",imgL)
        ##cv2.imshow("BM",disp)
        # ��ͼƬ��չ��3d�ռ��У���z�����ֵ��Ϊ��ǰ�ľ���
        threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32) / 16., camera_configs.Q)

        # ����������Ƭ  6/10  shape 22/84 float32
        cut_threeD = threeD[0:110:5, 60:480:10, 2]
        cut_threeD = cut_threeD / 10  # ����Ϊ����
        cut_threeD[cut_threeD > 1400] = 1400  # ���ƥ�����
        cut_threeD[cut_threeD < 0] = 1500  # ��Чֵ
        cut_threeD = cut_threeD.astype(np.uint16)  # ȡ�����ı���������
        cut_data = cut_threeD.reshape(924, 1)  # (462,1)  ʵʱͼ������

        cut_data_show = cut_threeD.copy()  # �����ʾ
        cut_data_show = cut_data_show / 5.88
        cut_data_show = cut_data_show.astype(np.uint8)
        ##cv2.imshow("Sampled at intervals", cut_data_show)

        cut_data_array = cut_data_array[:, 0:2]  # �޳���������
        cut_data_array = np.concatenate((cut_data, cut_data_array), axis=1)  # ��������ͼƬ
        cut_data_sequence = cut_data_array.copy()  # �������
        cut_data_sequence.sort(axis=1)  # ��������

        cut_data_mask = cut_data_sequence[:, 2]  # �������Mask
        cut_data_out = cut_data_sequence[:, 1]  # ��ֵ����
        cut_data_out[cut_data_mask > 1400] = 1500  # ����
        cut_data_out = cut_data_out.reshape(22, 42)  # ��������

        cut_data_show = cut_data_out.copy()  # �����ʾ
        cut_data_show = cut_data_show / 5.88
        cut_data_show = cut_data_show.astype(np.uint8)
        ##cv2.imshow("Noise reduction", cut_data_show)

        cut_data_out.sort(axis=0)  # ��������

        # ֻ�����������󷽾�����Ϣ
        # ��������������Ϣ��Ϊ��Ч��������ʾ
        ##cut_data_out[:, 0 : 19] = 1500
        ##cut_data_out[:, 26 : 42] = 1500

        deep_data = cut_data_out[4,:]           #���վ�������
        deep_data = deep_data.reshape(42)

        cut_data_show = cut_data_out.copy()  # �����ʾ
        cut_data_show = cut_data_show / 5.88
        cut_data_show = cut_data_show.astype(np.uint8)
        ##cv2.imshow("Sort by distance", cut_data_show)
        
        try:
            clear = bm_data.get_nowait()
        except:
            pass
        bm_data.put(deep_data)

        
        #cv2.imshow("disp", disp)
        # cv2.imshow("show right", Right)
        cv2.waitKey(1)
        #time.sleep(0.05)

    


# Ŀ����
def ObjectDetection(queue_camera_full, Object_data):
    while True:
        try:
            Left = queue_camera_full.get(1)
        except:
            continue
        # img=cp.Left
        img = Left
        # cv2.imshow("show Left", Left)
        # img =   #��ȡ����ԭͼ
        hog = cv2.HOGDescriptor()  # ����˵�Ĭ�ϼ����
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # SVM

        found, w = hog.detectMultiScale(img)  # ����ͼ��
        found_filtered = []

        # ��������������������м��Ŀ�������
        for ri, r in enumerate(found):
            for qi, q in enumerate(found):
                if ri != qi and is_inside(r, q):
                    break
                else:
                    found_filtered.append(r)
        
        try:
            clear = Object_data.get_nowait()
        except:
            pass
        Object_data.put(found_filtered)

        #cv2.imshow("people detection", img)
        #cv2.waitKey(1)




if __name__ == '__main__':

    # �����̴���Queue�������������ӽ���
    # parent_conn, child_conn = Pipe()
    queue_camera_bm = Queue(3)  # ����ͨѶ
    bm_data = Queue(3)  # ����ͨѶ
    queue_camera_full = Queue(3)  # ����ͨѶ
    queue_camera_show = Queue(3)  # ����ͨѶ
    Object_data = Queue(3)  # ����ͨѶ

    # �����ۺ���ʾģ������������ģ�鴫�ݾ�������
    bc = Queue()

    #����ͷ��ȡ(sgbmר�ã���Ա���)
    rc = Process(target=read_camera, args=(queue_camera_bm, queue_camera_full,queue_camera_show,))
    rc.start()

    bm = Process(target=BM, args=(queue_camera_bm, bm_data,))
    bm.start()

    obde = Process(target=ObjectDetection, args=(queue_camera_full, Object_data,))
    obde.start()

    show = Process(target=showImg, args=(queue_camera_show, bm_data, Object_data, bc, ))
    show.start()

    bcProcess = Process(target = broadcast, args = (bc, ))
    bcProcess.start()

    while True:
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        #time.sleep(0.5)
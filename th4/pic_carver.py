import re,zlib,cv2
from scapy.all import *

picture_directry="pictures"
faces_directry="faces"
pcap_file="bhp.pcap"

def get_http_headers(http_payload):
    try:
        headers_raw=http_payload[:http_payload.index("\r\n\r\n")+2]
        headers=dict(re.findall(r"(?P<name>.*?):(?P<value>.*?)\r\n",header_raw))
    except:
        return None
    if "Content-Type" not in headers:
        image=None
        image_type=None
        try:
            if "image" in headers['Content-type']:
                image_type=headers['Content-type'] .split('/')[1]
                image=http_payload [http_payload.index("\r\n\r\n")+4:]
                try:
                    if "Content-Encoding" in headers.keys():
                        if headers['Content-Encoding']=='gzip':
                            image=zlib.decompress(image,16+zlib.MAX_WBITS)
                        elif headers['Content-Encoding']=='deflate':
                            image=zlib.decompress(image)
                except:
                    pass
        except:
            return None,None

    return image,image_type

def face_detect(path,file_name):
    img=cv2.imread(path)
    cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    rects=cascade.detectMultiScale(img,1.3,4,cv2.cv.CV_HAAR_SCALE_IMAGE,(20,20))

    if len(rects)==0:
        return False
    rects[:,2:]+=rects[:,2:]
    for x1,y1,x2,y2 in rects:
        cv2.rectangle(img,(x1,y1),(x2,y2),(127,255,0),2)

    cv2.imwrite("{}/{}-{}".format(faces_directry,pcap_file.file_name,img)
    return True

def http_assembler(pcap_file):
    carved_images=0
    faces_detected=0

    a=rdpcap(pcap_file)
    sessions=a.session()

    for session in sessions:
        http_payload=''
        for packet in sessions[session]:
            try:
                if packet[TCP].dport==80 or packet[TCP].sport==80:
                    http_payload+=str(packet[TCP].payload)
            except:
                pass
        headers=get_http_headers(http_payload)
        
        if headers is None:
            continue
        image,image_type =extract_image(headers.http_payload)

        if image is not None and image_type is not None:
            file_names="{}-pic_carver_{}.{}".format(pcap_file,carved_images,image_type)

        with open("{}/{}".format(pictures_directry,file_name),"wb") as w:
            w.write(image)
        carved_images+=1

        try:
            result=face_detect("{}/{}".format(pictures_directry,file_name),file_name)

            if result is True:
                face_detect+=1
        except:
            pass
    return carved_images,faces_detected

carved_images,faces_detected=http_assembler(pcap_file)
print("Extracted:{} images".format(carved_images))
print("Detected:{} faces".format(faces_detected))

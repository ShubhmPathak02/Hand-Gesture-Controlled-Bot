import cv2
import mediapipe as mp
import socket

width = 1000
height = 1000
# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)

# Initialize MediaPipe Drawing utility
mp_drawing = mp.solutions.drawing_utils
def thumbs_up():
    if landmarks[4].y * height < landmarks[2].y * height :
         if landmarks[9].y * height -  landmarks[5].y * height > 3.200000000000:
           if landmarks[0].x * width > landmarks[9].x * width :
            if (landmarks[6].x * width < landmarks[8].x * width) & (landmarks[14].x * width < landmarks[16].x * width) :
             return "ALL THE BEST "
           else :
            if (landmarks[6].x * width > landmarks[8].x * width) & (landmarks[14].x * width > landmarks[16].x * width) :
             return "ALL THE BEST "
    return "none"


# Function to count fingers
def count_fingers(landmarks ):
    finger_tips = [8, 12, 16, 20 ]  # Index of finger tips in landmarks
    finger_base = [5, 9, 13, 17  ]   # Index of finger base in landmarks
    
    count = 0
    for tip, base in zip(finger_tips, finger_base):
       
        if landmarks[tip].y * height  < landmarks[base].y * height :
            count += 1
           
        
    if landmarks[5].x * width > landmarks[9].x * width :
        if (landmarks[4].x * width > landmarks[2].x * width) :
            count=count + 1
    else :
        if (landmarks[4].x * width < landmarks[2].x * width) :
            count=count + 1
    
    return count

esp_ip = '192.168.137.35'        
esp_port = 80

# # Keep the socket connection open during the whole session
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((esp_ip, esp_port))
    
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    last_message = b"none"
  
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("error")
            break

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe Hands
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks , results.multi_handedness:
                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Convert hand landmarks to a list of (x, y) coordinates
                landmarks = hand_landmarks.landmark

                fingers = thumbs_up()

                # Count fingers
                if fingers == "none" : 
                  fingers = count_fingers(landmarks)
                  cv2.putText(frame, f"Fingers: {fingers}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                
                else :
                    cv2.putText(frame, fingers , (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                

                # Determine the message to send based on the number of fingers
                message = b"none"
                match fingers:
                    case 1:
                        message = b"one\r"
                        if message != last_message:
                            s.sendall(message)
                            print(message)
                            last_message = message
                    case 2:
                        message = b"two\r"
                        if message != last_message:
                            s.sendall(message)
                            print(message)
                            last_message = message
                    case 3:
                        message = b"three\r"
                        if message != last_message:
                            s.sendall(message)
                            print(message)
                            last_message = message
                    case 4:
                        message = b"four\r"
                        if message != last_message:
                            s.sendall(message)
                            print(message)
                            last_message = message
                    case 0 :
                        message = b"zero\r"
                        if message != last_message:
                            s.sendall(message)
                            print(message)
                            last_message = message
 
        cv2.imshow('Frame', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
hands.close()

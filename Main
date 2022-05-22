import time
import cv2
import mediapipe as mp
import random

figure = ["ROCK", "PAPER", "SCISSORS"]


class Visor:
    def __init__(self):
        self.Draw = mp.solutions.drawing_utils
        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.image = None
        self.result = None

    def vision(self):
        with mp.solutions.hands.Hands(static_image_mode=False,
                                      max_num_hands=1,
                                      model_complexity=1
                                      ) as self.hands:
            while True:
                _, self.image = self.camera.read()
                self.result = self.hands.process(self.image)
                if self.result.multi_hand_landmarks:
                    print(game_logic(self.find_figure(self.result.multi_hand_landmarks)))

    def find_figure(self, multi_hand_landmarks):
        for id, lm in enumerate(multi_hand_landmarks[0].landmark):
            h, w, _ = self.image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(self.image, (cx, cy), 5, (0, 0, 255))
        self.Draw.draw_landmarks(self.image, self.result.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)
        PH = self.result.multi_hand_landmarks[0].landmark
        self.image = None
        self.result = None
        if is_paper(PH[8].y, PH[12].y, PH[16].y, PH[20].y, PH[6].y, PH[10].y, PH[14].y, PH[18].y):
            return "PAPER"
        elif is_scissors(PH[8].y, PH[12].y, PH[16].y, PH[20].y, PH[6].y, PH[10].y, PH[14].y, PH[18].y):
            return "PAPER"
        elif is_rock(PH[8].y, PH[12].y, PH[16].y, PH[20].y, PH[6].y, PH[10].y, PH[14].y, PH[18].y):
            return "ROCK"


def timer(image):  # timer for game readiness
    texts = ["Ready?", "3", "2", "1", "GO"]
    for text in texts:
        cv2.putText(img=image, text=text, org=(100, 100),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=3.0,
                    color=(255, 0, 0),
                    thickness=3
                    )
        time.sleep(0.5)
    return True


def is_paper(point_8, point_12, point_16, point_20, point_6, point_10, point_14, point_18):
    if (point_8 < point_6) and (point_12 < point_10) and (point_16 < point_14) and (point_20 < point_18):
        return True


def is_scissors(point_8, point_12, point_16, point_20, point_6, point_10, point_14, point_18):
    if (point_8 < point_6) and (point_12 < point_10) and (point_16 > point_14) and (point_20 > point_18):
        return True


def is_rock(point_8, point_12, point_16, point_20, point_6, point_10, point_14, point_18):
    if (point_8 > point_6) and (point_12 > point_10) and (point_16 > point_14) and (point_20 > point_18):
        return True


def computer_round():  # change computer answer
    return random.choice(figure)


def game_logic(player_input):  # game logic rock paper scissors
    computer_input = computer_round()
    print(f"{computer_input} - Computer ")
    print(f"{player_input} - Player")
    if computer_input == player_input:
        return "Draw"
    elif (computer_input == "PAPER") and (player_input == "ROCK"):
        return "Computer wins"
    elif (computer_input == "SCISSORS") and (player_input == "ROCK"):
        return "Player wins"
    elif (computer_input == "PAPER") and (player_input == "SCISSORS"):
        return "Player wins"
    elif (computer_input == "ROCK") and (player_input == "SCISSORS"):
        return "Computer wins"
    elif (computer_input == "ROCK") and (player_input == "PAPER"):
        return "Player wins"
    elif (computer_input == "SCISSORS") and (player_input == "PAPER"):
        return "Computer wins"


def run():
    visor = Visor()
    print(game_logic(visor.vision()))


def vision_cycle():
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    with mp.solutions.hands.Hands(static_image_mode=False,
                                  max_num_hands=1,
                                  model_complexity=1
                                  ) as hands:
        Draw = mp.solutions.drawing_utils

        while True:
            _, image = camera.read()
            result = hands.process(image)
            text = ""
            if result.multi_hand_landmarks:

                for id, lm in enumerate(result.multi_hand_landmarks[0].landmark):
                    h, w, _ = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(image, (cx, cy), 5, (0, 0, 255))
                    Draw.draw_landmarks(image, result.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)
                    PH = result.multi_hand_landmarks[0].landmark
                if is_paper(PH[8].y, PH[12].y, PH[16].y, PH[20].y, PH[6].y, PH[10].y, PH[14].y, PH[18].y):
                    text = "PAPER"
                    print(game_logic(text))
                elif is_scissors(PH[8].y, PH[12].y, PH[16].y, PH[20].y, PH[6].y, PH[10].y, PH[14].y, PH[18].y):
                    text = "SCISSORS"
                    print(game_logic(text))

                elif is_rock(PH[8].y, PH[12].y, PH[16].y, PH[20].y, PH[6].y, PH[10].y, PH[14].y, PH[18].y):
                    text = "ROCk"
                    print(game_logic(text))

            cv2.putText(img=image, text=text, org=(100, 100),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=3.0,
                        color=(255, 0, 0),
                        thickness=3
                        )
            cv2.imshow('Rock Paper Scissors', image)

            if cv2.waitKey(5) & 0xFF == 27:
                break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    vision_cycle()

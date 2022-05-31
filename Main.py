import cv2
import mediapipe as mp
import random

figure = ["ROCK", "PAPER", "SCISSORS"]


def find_figure(tuple_landmarks):
    def is_paper(point_8, point_12, point_16, point_20, point_6, point_10, point_14, point_18):
        if (point_8 < point_6) and (point_12 < point_10) and (point_16 < point_14) and (point_20 < point_18):
            return True

    def is_scissors(point_8, point_12, point_16, point_20, point_6, point_10, point_14, point_18):
        if (point_8 < point_6) and (point_12 < point_10) and (point_16 > point_14) and (point_20 > point_18):
            return True

    def is_rock(point_8, point_12, point_16, point_20, point_6, point_10, point_14, point_18):
        if (point_8 > point_6) and (point_12 > point_10) and (point_16 > point_14) and (point_20 > point_18):
            return True

    if is_paper(*tuple_landmarks):
        return "PAPER"
    elif is_scissors(*tuple_landmarks):
        return "SCISSORS"
    elif is_rock(*tuple_landmarks):
        return "ROCK"
    else:
        return "Not found"


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


def vision_cycle():
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    with mp.solutions.hands.Hands(static_image_mode=False,
                                  max_num_hands=1,
                                  model_complexity=1
                                  ) as hands:
        Draw = mp.solutions.drawing_utils
        clock = 0
        while True:
            _, image = camera.read()
            result = hands.process(image)

            def print_any_text(text):
                cv2.putText(img=image, text=text, org=(100, 100),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=3.0,
                            color=(255, 0, 0),
                            thickness=3
                            )

            def print_timer_text(number_word):
                texts = ["Ready?", "3", "2", "1", "GO!"]
                cv2.putText(img=image, text=texts[number_word], org=(100, 100),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=3.0,
                            color=(255, 0, 0),
                            thickness=3
                            )

            if result.multi_hand_landmarks:
                Draw.draw_landmarks(image, result.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS,
                                    mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
                                    mp.solutions.drawing_styles.get_default_hand_connections_style())
                PH = result.multi_hand_landmarks[0].landmark
                tuple_PH = (PH[8].y, PH[12].y, PH[16].y, PH[20].y, PH[6].y, PH[10].y, PH[14].y, PH[18].y)
            image = cv2.flip(image, 1)

            if clock < 15:
                print_timer_text(0)
            elif clock < 30:
                print_timer_text(1)
            elif clock < 45:
                print_timer_text(2)
            elif clock < 60:
                print_timer_text(3)
            elif clock < 75:
                print_timer_text(4)
            elif clock > 75 and result.multi_hand_landmarks:
                clock = 0
                answer = find_figure(tuple_PH)
                print_any_text(answer)
                print(game_logic(answer))
            else:
                print_any_text("Not found")
            clock += 1
            cv2.imshow('Rock Paper Scissors', image)

            if cv2.waitKey(5) & 0xFF == 27:
                break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    vision_cycle()

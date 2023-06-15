import time

def flappy_bird():
    score = 0
    bird_position = 10
    game_over = False

    while not game_over:
        print("Score: ", score)
        print(" " * bird_position + "🐦")

        command = input("Press any key to flap or 'q' to quit.")

        if command == 'q':
            break

        bird_position += 1
        score += 1

        if bird_position >= 40:
            print("Game Over!")
            game_over = True

        time.sleep(0.1)

flappy_bird()

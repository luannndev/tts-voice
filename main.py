from gtts import gTTS
import pygame
import os


def text_to_speech(text, lang='de'):
    tts = gTTS(text=text, lang=lang, slow=False)
    filename = 'output.mp3'
    tts.save(filename)
    print(f"Die Audiodatei wurde als '{filename}' gespeichert.")
    return filename


def play_sound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Warten, bis das Audio fertig ist
    while pygame.mixer.music.get_busy():
        continue


def main():
    text = input("Gib den Text ein, den du umwandeln möchtest: ")
    filename = text_to_speech(text)

    play_choice = input("Möchtest du die Audiodatei jetzt abspielen? (ja/nein): ").strip().lower()
    if play_choice == 'ja':
        play_sound(filename)


if __name__ == "__main__":
    main()

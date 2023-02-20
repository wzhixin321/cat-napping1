def on_gesture_tilt_left():
    basic.show_number(randint(1, 12))
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_a():
    basic.show_number(input.temperature())
    basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_number(randint(1, 6))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_free_fall():
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            500,
            499,
            255,
            0,
            750,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_button_pressed_b():
    music.play_melody("B B B B A G F E ", 120)
    basic.pause(1000)
    music.ring_tone(262)
    basic.pause(1000)
    music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)

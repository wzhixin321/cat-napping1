input.onGesture(Gesture.TiltLeft, function () {
    basic.showNumber(randint(1, 12))
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
    basic.pause(1000)
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        `)
    basic.showLeds(`
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function () {
    music.playMelody("B B B B A G F E ", 120)
    basic.pause(1000)
    music.ringTone(262)
    basic.pause(1000)
    music.stopAllSounds()
})

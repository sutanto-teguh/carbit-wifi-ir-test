function Mundur () {
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.analogWritePin(AnalogPin.P8, 0)
    pins.analogWritePin(AnalogPin.P9, 150)
    pins.analogWritePin(AnalogPin.P12, 150)
    pins.analogWritePin(AnalogPin.P15, 0)
}
function Kanan () {
    pins.digitalWritePin(DigitalPin.P11, 1)
    pins.analogWritePin(AnalogPin.P8, 150)
    pins.analogWritePin(AnalogPin.P9, 0)
    pins.analogWritePin(AnalogPin.P12, 150)
    pins.analogWritePin(AnalogPin.P15, 0)
}
function Maju () {
    pins.digitalWritePin(DigitalPin.P11, 1)
    pins.analogWritePin(AnalogPin.P8, 150)
    pins.analogWritePin(AnalogPin.P9, 0)
    pins.analogWritePin(AnalogPin.P12, 0)
    pins.analogWritePin(AnalogPin.P15, 150)
}
function Kiri () {
    pins.digitalWritePin(DigitalPin.P11, 1)
    pins.analogWritePin(AnalogPin.P8, 0)
    pins.analogWritePin(AnalogPin.P9, 150)
    pins.analogWritePin(AnalogPin.P12, 0)
    pins.analogWritePin(AnalogPin.P15, 150)
}
function Stop () {
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.analogWritePin(AnalogPin.P8, 0)
    pins.analogWritePin(AnalogPin.P9, 0)
    pins.analogWritePin(AnalogPin.P12, 0)
    pins.analogWritePin(AnalogPin.P15, 0)
}
makerbit.connectIrReceiver(DigitalPin.P16, IrProtocol.OSOYOO)
basic.forever(function () {
    if (makerbit.irButton() == 24) {
        Maju()
    }
    if (makerbit.irButton() == 56) {
        Stop()
    }
    if (makerbit.irButton() == 74) {
        Mundur()
    }
    if (makerbit.irButton() == 16) {
        Kiri()
    }
    if (makerbit.irButton() == 90) {
        Kanan()
    }
})

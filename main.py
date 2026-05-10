def Mundur():
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P9, 1)
    pins.digital_write_pin(DigitalPin.P11, 1)
    pins.digital_write_pin(DigitalPin.P15, 0)
def Kanan():
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P12, 1)
    pins.analog_write_pin(AnalogPin.P5, 423)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.analog_write_pin(AnalogPin.P11, 423)
    pins.digital_write_pin(DigitalPin.P15, 0)
def Maju():
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.digital_write_pin(DigitalPin.P5, 1)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.digital_write_pin(DigitalPin.P15, 1)
def Kiri():
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.analog_write_pin(AnalogPin.P9, 423)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.analog_write_pin(AnalogPin.P15, 423)
def Stop():
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.digital_write_pin(DigitalPin.P15, 0)
pins.digital_write_pin(DigitalPin.P5, 0)
pins.digital_write_pin(DigitalPin.P9, 0)
pins.digital_write_pin(DigitalPin.P11, 0)
pins.digital_write_pin(DigitalPin.P15, 0)
makerbit.connect_ir_receiver(DigitalPin.P16, IrProtocol.OSOYOO)

def on_forever():
    if makerbit.ir_button() == 24:
        Maju()
    if makerbit.ir_button() == 56:
        Stop()
    if makerbit.ir_button() == 74:
        Mundur()
    if makerbit.ir_button() == 16:
        Kiri()
    if makerbit.ir_button() == 90:
        Kanan()
basic.forever(on_forever)

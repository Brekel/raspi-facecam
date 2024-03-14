import socket
import select
import board
import neopixel
import socket

def get_hostname_value():
    hostname = socket.gethostname()
    prefix = "raspicam"

    if hostname.startswith(prefix):
        number_part = hostname[len(prefix):]
        if not number_part:
            return 0

        try:
            number = int(number_part)
            if 0 <= number <= 9:
                return number
            else:
                return -1
        except ValueError:
            return -1
    else:
        return -1


def listen_for_broadcasts(port=9875):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(('', port))
    sock.setblocking(0)

    device_id = get_hostname_value();
    print(f"device_id: {device_id}")

    print(f"Listening for broadcast packets on port {port}...")

    pixels = neopixel.NeoPixel(board.D18, 12, pixel_order=neopixel.GRBW)
    pixels.brightness = 0.02
    pixels.fill((0, 0, 0, 255))

    try:
        while True:
            readable, _, _ = select.select([sock], [], [], 1.0)

            if readable:
                message, addr = sock.recvfrom(1024)
                message = message.decode()

                if message.startswith("BREKEL_START\t") and message.endswith("\tBREKEL_END"):
                    parts = message.split('\t')
                    if len(parts) == 8 and parts[0] == "BREKEL_START" and parts[7] == "BREKEL_END":
                        try:
                            red = int(parts[1])
                            green = int(parts[2])
                            blue = int(parts[3])
                            white = int(parts[4])
                            brightness = float(parts[5])
                            device = int(parts[6])
                            if device == device_id:
                                print(f"Received RGBW: ({red}, {green}, {blue}, {white}), Brightness: {brightness}")
                                pixels.brightness = brightness
                                pixels.fill((red, green, blue, white))
                        except ValueError as e:
                            print(f"Error parsing values: {e}")
    except KeyboardInterrupt:
        print("Program stopped by user.")
    finally:
        sock.close()

if __name__ == "__main__":
    listen_for_broadcasts()
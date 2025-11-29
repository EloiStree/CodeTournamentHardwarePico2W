Need: https://github.com/EloiStree/APIntCodeTournamentPythonRelay/blob/main/README.md

------------

# Code Tournament Hardware – Pico 2W

A Pico 2W setup for use in a code tournament.

I’m planning to organize a code tournament, and for that I intend to use the Raspberry Pi Pico 2W in two main roles:

### 1. Input Hacking

The Pico 2W should be able to:

* Emulate a keyboard
* Emulate a mouse
* Emulate a gamepad for uncommon games (non-XInput)

### 2. Python Code Sandbox

The Pico 2W will act as a small sandbox capable of receiving, running, and returning results from user-submitted Python code. It will need to support:

* **Update server target:**

  * Allow changing the mDNS address (e.g., `raspberrypi.local`)
* **Update code logic:**

  * Replace the main script with the player’s submitted code
* **Run logic code:**

  * Execute the player’s script safely
* **UDP communication:**

  * Receive input via UDP (bytes or text)
  * Send input or state via UDP using a simple byte protocol (IID S2W)
* **WebSocket communication:**

  * WebGL supports WebSockets, so the Pico 2W should be able to:

    * Send input over WebSockets using the IID S2W format
    * Receive game state information (bytes or text) over WebSockets



Previous Code draft code: 
- Gamepad and keyboard : https://github.com/EloiStree/2024_11_16_WowIntegerWorkshopPicoW.git
- 0H Gamejam MQTT : https://github.com/EloiStree/2025_10_26_GameJam0H







------------


Step:  
- Install the https://circuitpython.org/board/raspberry_pi_pico2_w/ on Your Pico2W

# X, Y coordinates for various UI elements in a game or application.
from helpers import AutoSBC, AvailableSBCs, SBC


def sbc_script():
    SBC.initial_wait()
    SBC.open_sbc(sbc_type=AvailableSBCs.EIGHT_THREE_PLUS)
    SBC.wait_for_sbc_to_open(wait_time=2)

    AutoSBC.click_on_logo()
    AutoSBC.click_on_build()

    SBC.submit_sbc()
    SBC.claim_reward()


def pick_83_plus():
    try:
        while True:
            sbc_script()
    except Exception as e:
        print(f"Script stopped by the user.")

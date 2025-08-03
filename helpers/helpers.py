from lib import pyautogui
import time

# === Constants for waiting times ===
# seconds before starting the script
SQUAD_BUILDER_WAIT = 2  # seconds
WAIT_FOR_BUILD_COMPLETE = 3  # seconds after clicking build


class AvailableSBCs:
    TOTW = "TOTW"
    EIGHT_THREE_PLUS = "83+"


# === General SBC Functions ===
class SBC:
    # Waiting ===
    INITIAL_WAIT = 2
    WAIT_FOR_SBC_OPEN = 3  # wait to load the SBC
    WAIT_AFTER_SUBMIT = 2  # wait after submitting SBC
    WAIT_AFTER_CLAIM = 0.5  # wait after claiming SBC

    # Coordinates for SBC elements
    TOTW_SBC_CELL = 730, 758
    SUBMIT_BUTTON = 1427, 989
    CLAIM_BUTTON = 955, 765

    @classmethod
    def open_sbc(cls, sbc_type: str):
        if sbc_type == AvailableSBCs.TOTW:
            pyautogui.moveTo(cls.TOTW_SBC_CELL)
            pyautogui.click()
        else:
            raise ValueError(f"Unsupported SBC type: {sbc_type}")

        time.sleep(cls.WAIT_FOR_SBC_OPEN)  # Wait for the SBC to open

    @classmethod
    def initial_wait(cls):
        """  Initial wait before starting the script. """
        time.sleep(cls.INITIAL_WAIT)

    @classmethod
    def submit_sbc(cls):
        pyautogui.moveTo(cls.SUBMIT_BUTTON)
        pyautogui.click()
        time.sleep(cls.WAIT_AFTER_SUBMIT)

    @classmethod
    def claim_reward(cls):
        pyautogui.moveTo(cls.CLAIM_BUTTON)
        pyautogui.click()
        time.sleep(cls.WAIT_AFTER_CLAIM)


# === Squad Builder ===
class SquadBuilder:
    """
    Workflow:
    - Click on Squad Builder button
    - Click on Ignore Position Slider
    - Set Max/Min OVR
    - !IMPORTANT! Scroll down to the bottom of the list
    - Click on Build button
    """

    SQUAD_BUILDER_BUTTON = 1643, 876
    IGNORE_POSITION_SLIDER_ON = 1792, 589

    MAX_OVR_CELL = 1726, 864
    OUTSIDE_BOX = 1867, 759

    BUILD_BUTTON = 1717, 985

    PAUSES_WITHIN_SQUAD_BUILDER = 0.4  # seconds. Because it's on front, no long waitings

    @classmethod
    def _wait_after_interaction(cls):
        time.sleep(cls.PAUSES_WITHIN_SQUAD_BUILDER)

    @classmethod
    def click_on_squad_builder(cls):
        pyautogui.moveTo(cls.SQUAD_BUILDER_BUTTON)
        pyautogui.click()

        cls._wait_after_interaction()

    @classmethod
    def click_on_ignore_position_slider(cls):
        pyautogui.moveTo(cls.IGNORE_POSITION_SLIDER_ON)
        pyautogui.click()

        cls._wait_after_interaction()

    @classmethod
    def sort_low_to_high(cls):
        ...  # To be implemented later

    @classmethod
    def set_max_ovr(cls, ovr):
        pyautogui.moveTo(cls.MAX_OVR_CELL)
        pyautogui.click()
        pyautogui.write(str(ovr), interval=0.05)

        cls._wait_after_interaction()
        cls._click_outside_the_box()  # Click outside the box to save the input

    @classmethod
    def _click_outside_the_box(cls):
        """
        Because EA is a garage of degenerates, you can't submit just like this.
        You need to click outside the box to save the max or min ovr input.
        """
        pyautogui.moveTo(cls.OUTSIDE_BOX)
        pyautogui.click()

    @classmethod
    def scroll_down(cls):
        pyautogui.moveTo(cls.MAX_OVR_CELL)
        pyautogui.scroll(-700)
        cls._wait_after_interaction()

    @classmethod
    def click_on_build(cls):
        pyautogui.moveTo(cls.BUILD_BUTTON)
        pyautogui.click()

        time.sleep(WAIT_FOR_BUILD_COMPLETE)  # Wait for the build to complete

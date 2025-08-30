from lib import pyautogui
import time

# === Constants for waiting times ===
# seconds before starting the script
SQUAD_BUILDER_WAIT = 2  # seconds
WAIT_FOR_BUILD_COMPLETE = 3  # seconds after clicking build


class AutoSBC:
    LOGO = 213, 315
    BUILD = 956, 725

    @classmethod
    def click_on_logo(cls, wait_time=0.2):
        pyautogui.moveTo(cls.LOGO)
        pyautogui.click()
        time.sleep(wait_time)

    @classmethod
    def click_on_build(cls, wait_time=2):
        pyautogui.moveTo(cls.BUILD)
        pyautogui.click()
        time.sleep(wait_time)  # Wait for the build to complete



class AvailableSBCs:
    TOTW = "TOTW"
    TOTW_SBC_CELL = 730, 758

    EIGHT_THREE_PLUS = "83+"
    EIGHT_THREE_SBC_CELL = 732, 451

    EIGHTY_NINE_PLUS = "89+"
    EIGHTY_NINE_SBC_CELL = 1218, 750


# === General SBC Functions ===
class SBC:
    # Waiting ===
    INITIAL_WAIT = 2
    WAIT_FOR_SBC_OPEN = 3  # wait to load the SBC
    WAIT_AFTER_SUBMIT = 2  # wait after submitting SBC
    WAIT_AFTER_CLAIM = 0.5  # wait after claiming SBC

    SUBMIT_BUTTON = 1427, 989
    CLAIM_BUTTON = 955, 765

    @classmethod
    def wait_for_sbc_to_open(cls, wait_time: int = WAIT_FOR_SBC_OPEN):
        time.sleep(wait_time)

    @classmethod
    def open_sbc(cls, sbc_type: str):
        if sbc_type == AvailableSBCs.TOTW:
            sbc_cell: tuple[int, int] = AvailableSBCs.TOTW_SBC_CELL

        elif sbc_type == AvailableSBCs.EIGHTY_NINE_PLUS:
            sbc_cell: tuple[int, int] = AvailableSBCs.EIGHTY_NINE_SBC_CELL

        elif sbc_type == AvailableSBCs.EIGHT_THREE_PLUS:
            sbc_cell: tuple[int, int] = AvailableSBCs.EIGHT_THREE_SBC_CELL

        else:
            raise ValueError(f"Unsupported SBC type: {sbc_type}")

        pyautogui.moveTo(sbc_cell)
        pyautogui.click()

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
    IGNORE_POSITION_SLIDER_ON = 1789, 590

    SORT_BY_DROPDOWN = 1686, 660
    SORT_BY_LOW_TO_HIGH = 1635, 850

    MAX_OVR_CELL = 1726, 864
    MIN_OVR_CELL = 1529, 858

    OUTSIDE_BOX = 1867, 759

    BUILD_BUTTON = 1717, 985

    PAUSES_WITHIN_SQUAD_BUILDER = 0.4  # seconds. Because it's on front, no long waitings

    @classmethod
    def _wait_after_interaction(cls):
        time.sleep(cls.PAUSES_WITHIN_SQUAD_BUILDER)

    @classmethod
    def click_on_squad_builder(cls):
        """Clicks on 'Use Squad Builder' button."""
        pyautogui.moveTo(cls.SQUAD_BUILDER_BUTTON)
        pyautogui.click()

        cls._wait_after_interaction()

    @classmethod
    def click_on_ignore_position_slider(cls):
        pyautogui.moveTo(cls.IGNORE_POSITION_SLIDER_ON)
        cls._wait_after_interaction()
        pyautogui.click()

        cls._wait_after_interaction()

    @classmethod
    def sort_low_to_high(cls):
        cls._wait_after_interaction()

        pyautogui.moveTo(cls.SORT_BY_DROPDOWN)
        cls._wait_after_interaction()
        pyautogui.click()

        pyautogui.moveTo(cls.SORT_BY_LOW_TO_HIGH)
        cls._wait_after_interaction()
        pyautogui.click()


    @classmethod
    def set_max_ovr(cls, ovr):
        pyautogui.moveTo(cls.MAX_OVR_CELL)
        time.sleep(cls.PAUSES_WITHIN_SQUAD_BUILDER)
        pyautogui.click()
        pyautogui.write(str(ovr), interval=0.05)

        cls._wait_after_interaction()
        cls._click_outside_the_box()  # Click outside the box to save the input

    @classmethod
    def set_min_ovr(cls, ovr):
        """ Sets the minimum OVR in the Squad Builder. """
        pyautogui.moveTo(cls.MIN_OVR_CELL)
        time.sleep(cls.PAUSES_WITHIN_SQUAD_BUILDER)
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

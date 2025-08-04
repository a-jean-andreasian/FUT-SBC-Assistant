from helpers import SBC, AvailableSBCs, SquadBuilder


def eighty_nine_squadshifter_build(min_ovr: str = "89"):
    SBC.initial_wait()
    SBC.open_sbc(sbc_type=AvailableSBCs.EIGHTY_NINE_PLUS)

    SquadBuilder.click_on_squad_builder()
    SquadBuilder.click_on_ignore_position_slider()

    SquadBuilder.sort_low_to_high()

    SquadBuilder.set_min_ovr(min_ovr)

    SquadBuilder.scroll_down()

    SquadBuilder.click_on_build()

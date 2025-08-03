from helpers import SquadBuilder, SBC, AvailableSBCs


def totw_build():
    SBC.initial_wait()  # wait before starting the script

    # ==== Clicking on SBC ====
    SBC.open_sbc(sbc_type=AvailableSBCs.TOTW)

    # ==== Clicking on Squad Builder ====
    SquadBuilder.click_on_squad_builder()
    SquadBuilder.click_on_ignore_position_slider()
    SquadBuilder.set_max_ovr("83")
    SquadBuilder.scroll_down()
    SquadBuilder.click_on_build()

    SBC.submit_sbc()
    SBC.claim_reward()

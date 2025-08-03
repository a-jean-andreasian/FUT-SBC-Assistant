from src.eight_three_plus_pick import pick_83_plus
from src.totw_untrade import totw_build


if __name__ == "__main__":
    choice = input(
        "Press 1 for Auto 83+ Pick script\n"
        "Press 2 for Auto TOTW Build script\n"
    )

    if choice == "1" or choice == "":
        pick_83_plus()
    elif choice == "2":
        totw_build()

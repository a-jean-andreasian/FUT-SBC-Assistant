import argparse
from src.eight_three_plus_pick import pick_83_plus
from src.totw_untrade import totw_build
from src.eighty_nine_squadshifter import eighty_nine_squadshifter_build

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--option",
                        type=int,
                        choices=[1, 2, 3],
                        help="1 for 83+ Pick, 2 for TOTW Build, 3 for 89+ Squadshifter")

    parser.add_argument("--min-ovr",
                        type=int,
                        help="Minimum OVR for 89+ Squadshifter (only applies to --option 3)")


    args = parser.parse_args()

    # fallback to interactive input if --option wasn't passed
    if args.option is None:
        try:
            user_input = input(
                "Press 1 for Auto 83+ Pick script\n"
                "Press 2 for Auto TOTW Build script\n"
                "Press 3 for Auto 89+ Squadshifter Build script\n"
                "Choice: "
            )
            option = int(user_input.strip()) if user_input.strip() else 1
        except ValueError:
            option = 1
    else:
        option = args.option

    # main logic
    if option == 1:
        pick_83_plus()
    elif option == 2:
        totw_build()
    elif option == 3:
        if args.min_ovr:
            eighty_nine_squadshifter_build(args.min_ovr)
        else:
            eighty_nine_squadshifter_build()

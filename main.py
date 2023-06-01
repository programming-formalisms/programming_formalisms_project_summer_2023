"""The Programming Formalisms Project 2023.

Project used in the UPPMAX Programming Formalisms course.
"""
import cProfile

from pfp2023_richelbilderbeek.testing import (
    get_datas,
    get_sorting_functions,
    get_speed_measurements,
    save_speed_measurements,
)

if __name__ == "__main__":
    speed_measurements = get_speed_measurements(
        datas = get_datas(data_lengths = [2, 4, 6, 8, 10]),
        functions = get_sorting_functions(),
    )
    save_speed_measurements(speed_measurements, "speeds.csv")

    cProfile.run(
        "get_speed_measurements("
        "datas = get_datas(data_lengths = [2, 4, 6, 8, 10]), "
        "functions = get_sorting_functions())",
    )


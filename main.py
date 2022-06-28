from ellevator import Elevator


if __name__ == '__main__':
    e = Elevator()

    e.elevator_status()
    e.accept_summon_input()
    e.accept_exit_input()

    while len(e.dests.keys()) > 0:

        e.determine_direction()
        e.move()

        open = e.check_door_open()

        if open:
            e.accept_summon_input()
            e.accept_exit_input()

        e.determine_direction()

        open = e.check_door_open()

        if open:
            e.accept_summon_input()
            e.accept_exit_input()

    e.reset()

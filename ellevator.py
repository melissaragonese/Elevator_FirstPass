import time

min_floor = 1
max_floor = 10
door_string = 'Doors opening on floor {}. Current direction is {}. Current destinations are: {}'
moving_string = 'Moving {} to floor {}'
exit_input_string = 'CHOOSE DESTINATION: Please select a destination from floors {} through {} or type "pass" to ' \
                    'decline passing ' \
                      'input: '
summon_input_string_floor = 'SUMMON: Which floor are you on? Please select from floors {} through {} or type "pass" ' \
                            'to decline ' \
                      'input: '
summon_input_string_dir = 'SUMMON: Would you like to go up or down? Please type "up" to go up, "down" to go down, or ' \
                          '"pass" ' \
                          'to decline input: '


class Elevator(object):

    def __init__(self):

        self.current_floor = min_floor
        self.dests = {

        }
        # self.dests = {
        #     4: 'up',
        #     3: 'down',
        #     6: 'up',
        #     1: 'down',
        #     0: 'up',
        #     0: 'exit',
        #     9: 'exit'
        # }
        self.dir = 'up'

    def determine_direction(self):
        if len(self.dests.keys()) == 0:
            self.dir = 'down'
        elif max(self.dests.keys()) > self.current_floor and self.dir == 'up':
            self.dir = 'up'
        elif min(self.dests.keys()) < self.current_floor and self.dir == 'down':
            self.dir = 'down'
        elif min(self.dests.keys()) >= self.current_floor and self.dir == 'down':
            self.dir = 'up'
        else:
            self.dir = 'down'

    def check_door_open(self):

        if (self.current_floor in self.dests and self.dests[self.current_floor] == self.dir) | \
                (self.current_floor in self.dests and self.dests[self.current_floor] == 'exit'):
            del self.dests[self.current_floor]
            print(door_string.format(self.current_floor, self.dir, list(set(self.dests.keys()))))
            return True
        else:
            return False

    def move(self):
        if self.dir == 'up' and self.current_floor != max_floor:
            print(moving_string.format(self.dir, self.current_floor + 1))
            self.current_floor += 1
        else:
            print(moving_string.format(self.dir, self.current_floor - 1))
            self.current_floor -= 1

    def reset(self):
        self.current_floor = min_floor
        self.dests = {
        }
        self.dir = 'up'
        print('Elevator Reset. ' + door_string.format(self.current_floor, self.dir, list(set(self.dests.keys()))))

    def elevator_status(self):
        dests_to_print = [str(x) for x in self.dests.keys()]
        print('The elevator is moving in the {} direction'.format(self.dir))
        print('The elevator is on floor {}'.format(self.current_floor))
        print('The elevator is currently heading to floor(s) {}'.format((", ".join(dests_to_print))))

    def accept_exit_input(self):
        while True:
            next_dest = input(exit_input_string.format(min_floor, max_floor))
            if next_dest.isdigit() and min_floor <= int(next_dest) <= max_floor:
                self.dests[int(next_dest)] = 'exit'
                break
            elif next_dest.lower() == 'pass':
                break
            else:
                print('Your response must be a digit between {} and {}, or "pass"'.format(min_floor, max_floor))

    def accept_summon_input(self):
        while True:
            summon_floor = input(summon_input_string_floor.format(min_floor, max_floor))
            if (summon_floor.isdigit() and min_floor <= int(summon_floor) <= max_floor) \
                    or summon_floor.lower() == 'pass':
                break
            else:
                print('Your response must be a digit between {} and {}, or "pass"'.format(min_floor, max_floor))

        while True:
            if summon_floor.lower() == 'pass':
                break

            summon_dir = input(summon_input_string_dir)
            if summon_dir in ['up', 'down']:
                self.dests[int(summon_floor)] = summon_dir
                break
            elif summon_dir.lower() == 'pass':
                break
            else:
                print("Your response must be /'up/', /'down/', or /'pass/'")

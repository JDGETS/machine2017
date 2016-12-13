__author__ = 'capra'

from inputs import get_gamepad

a = True

class ControllerMachina(object):
    """
    Mapping of actions:
    BTN_SOUTH_1 : A
    BTN_NORTH_1 : X
    BTN_WEST_1 : Y
    BTN_EAST_1 : B
    ABS_HAT0Y_-1 : D-pad up
    ABS_HAT0Y_1 : D-pad down
    ABS_HAT0X_1 : D-pad right
    ABS_HAT0X_-1 : D-pad left
    """
    def __init__(self):
        self._mapper = {}
        self._add_function('BTN_SOUTH_1', self._a_button)
        self._add_function('BTN_NORTH_1', self._x_button)
        self._add_function('BTN_WEST_1', self._y_button)
        self._add_function('BTN_EAST_1', self._b_button)
        self._add_function('ABS_HAT0Y_-1', self._dpad_up)
        self._add_function('ABS_HAT0Y_1', self._dpad_down)
        self._add_function('ABS_HAT0X_1', self._dpad_right)
        self._add_function('ABS_HAT0X_-1', self._dpad_left)

    def _add_function(self, key, function):
        self._mapper[key] = function

    def _a_button(self):
        """
        Moves the trigger down (pushes the ball)
        :return:
        """
        print 'Pressing A'

    def _b_button(self):
        """
        Moves the trigger up
        :return:
        """
        print 'Pressing B'

    def _x_button(self):
        print 'Pressing X'

    def _y_button(self):
        print 'Pressing Y'

    def _dpad_up(self):
        print 'Pressing up'

    def _dpad_down(self):
        print 'Pressing down'

    def _dpad_right(self):
        print 'Pressing right'

    def _dpad_left(self):
        print 'Pressing left'

    def do_action(self, action):

        try:
            self._mapper[self._convert_action_to_key(action)]()
        except KeyError:
            pass

    def _convert_action_to_key(self, action):
        key = action[0] + '_' + str(action[1])
        print 'dic key is: ', key
        return key

def do_a_button():
    print "doing the a button stuff"

leController = ControllerMachina()

while a:
    events = get_gamepad()
    for event in events:
        #print event.ev_type, event.code, event.state
        #if event.ev_type == 'Key' and event.code == "BTN_SOUTH" and event.state == 1:
        gamepad_action = (event.code, event.state)
        #print 'event.code: ', event.code
        #print 'event.state: ', event.state
        #print 'gamepad_action: ', gamepad_action
        if event.state == 1 or event.state == -1:
            leController.do_action(gamepad_action)

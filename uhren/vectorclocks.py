# General class representing a process with a logical clock
# Date: 07.01.2021
# Author: ZuS


class Process:

    def __init__(self, name, proc_n, id):
        self.lc_value = []
        for i in range(0, proc_n):
            self.lc_value.append(0)
        self.id = id
        self.name = name

    def handle_event(self, event):
        self.lc_value[self.id] += 1

    def handle_message(self, message):
        # merge clocks
        for i in range(0, len(self.lc_value)):
            self.lc_value[i] = max(self.lc_value[i], message.get_time()[i])

        # Raise an event to process the message
        self.handle_event(self.get_name()+": "+message.get_message())

    def get_name(self):
        return self.name

    def get_lc(self):
        return self.lc_value

# General class representing a message with a logical time stamp
# Date: 07.01.2021
# Author: ZuS


class Message:

    def __init__(self, message, time):
        self.message = message
        self.time = time

    def get_message(self):
        return self.message

    def get_time(self):
        return self.time

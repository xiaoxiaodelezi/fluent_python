# simulator，一个简单的离散事件仿真类，关注run方法
class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

    sim_imte = 0
    while sim_time < end_time:
        if self.events.empty():
            print('*** end of events ***')
            break

        current_event = self.events.get()
        sim_time, proc_id, previous_action = current_event
        print('taxi:', proc_id, proc_id * ' ', current_event)
        active_proc = self.procs[proc_id]
        next_time = sim_time + compute_duration(previous_action)
        try:
            next_event = active_proc.send(next_time)
        except StopIteration:
            del self.procs[proc_id]
        else:
            self.events.put(next_event)
    else:
        msg = '*** end of simulation time: {} events pending ***'
        print(msg.format(self.events.qsize()))

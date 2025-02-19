class Process:
    def __init__(self, name, arrival_time, total_executions):
        self.name = name
        self.arrival_time = arrival_time
        self.total_executions = total_executions
        self.finish_time = 0
        self.executions = 0
        self.wait_time = 0

    def has_finished(self) -> bool:
        if self.executions == self.total_executions:
            return True
        return False

    def execute(self) -> None:
        self.executions += 1


def sort_processes_by_arrival_time(processes: list[Process]):
    """
    sorts a given a list of Process instances by the arrival
    time of the processes
    """
    return sorted(processes, key=lambda p: p.arrival_time)


def get_new_processes(time, slept_processes: list[Process]):
    """
    Returns a list of the processes which arrival_time is the
    same as the given time and updates the slept_processes list
    by removing the new processes from it
    """
    new_processes = [p for p in slept_processes if p.arrival_time == time]
    slept_processes = [p for p in slept_processes if p not in new_processes]
    return new_processes, slept_processes


def get_processes_names(processes: list[Process]):
    return [process.name for process in processes]


def swap_processes(processes: list[Process], i, j):
    """
    swaps the process at index i with the process at index j
    """
    processes[i], processes[j] = processes[j], processes[i]


def find_first_processes(processes: list[Process]):
    """
    Finds all the processes that arrive first
    """
    sorted_proccesses = sort_processes_by_arrival_time(processes)
    first_arrival_time = sorted_proccesses[0].arrival_time
    first_processes = []
    for process in sorted_proccesses:
        if process.arrival_time != first_arrival_time:
            return first_processes
        first_processes.append(process)

    return first_processes

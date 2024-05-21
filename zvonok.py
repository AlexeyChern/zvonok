workers = dict()


class WrongHoursException(BaseException):
    """Exception for not valid hours"""
    pass


class WorkerHours:
    """Class describing workers and their hours"""
    name: str
    hours: str
    sum_hours: int

    def __init__(self, worker_line):
        try:
            res = worker_line.rsplit(' ', 1)
            self.name = res[0]
            cur_hours = int(res[1])
            if cur_hours > 24 or cur_hours < 1:
                raise WrongHoursException
            if self.name in workers:
                self.hours = workers[self.name].hours + ', ' + str(cur_hours)
                self.sum_hours = workers[self.name].sum_hours + cur_hours
            else:
                self.hours = str(cur_hours)
                self.sum_hours = cur_hours
            workers[self.name] = self
        except WrongHoursException: ## значит часы не валидны
            pass
        except IndexError: ## значит часов нет
            pass
        except ValueError: ## Значит часы не являются числом
            pass


def get_name_and_hours(text_line) -> WorkerHours:
    cur_worker = WorkerHours(text_line)
    return cur_worker


def parse_and_print_result(result_workers):
    for key in result_workers:
        item = result_workers[key]
        print(f'{item.name}: {item.hours}; sum: {item.sum_hours}')


filename = 'jobs.txt'
with open(filename, 'r') as file:  ### Данные берутся из файла.
    line = file.readline()
    while line:
        processing = get_name_and_hours(line)
        line = file.readline()

parse_and_print_result(workers)

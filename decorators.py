import time

def activity_logger(original_function):
    def run_function():
        print("Function Started")
        original_function()
        print("Function Ended")
    return run_function


@activity_logger
def show_message():
    print("Welcome Students")


show_message()


is_logged_in = True


def login_required(original_function):
    def run_function():
        if is_logged_in:
            original_function()
        else:
            print("Please Login First")
    return run_function


@login_required
def open_profile():
    print("Welcome to Your Profile")


open_profile()



def execution_timer(original_function):
    def run_function():
        start_time = time.time()
        original_function()
        end_time = time.time()
        print("Execution Time =", end_time - start_time, "seconds")
    return run_function


@execution_timer
def process_numbers():
    for number in range(1000000):
        pass


process_numbers()
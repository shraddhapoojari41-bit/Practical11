def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

def get_result(marks):
    # Assuming average >= 40 is a PASS based on your test cases
    average = calculate_average(marks)
    if average >= 40:
        return "PASS"
    else:
        return "FAIL"

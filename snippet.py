import argparse

def get_args():
    """ Get the arguments passed in the command line and return it as dict and str respectively""""
    
    parser = argparse.ArgumentParser(description='Pass two numbers and a operation to perform on them')
    
    parser.add_argument('--first_number', type=int, help='First Number')
    parser.add_argument('--second_number',type=int, help='Second Number')
    parser.add_argument('--operation', type=str, help='operation')

    args = parser.parse_args()

    return {"x": args.first_number, "y": args.second_number}, args.operation


def check_posted_data(posted_data, function_name):
    """ Validating the posted data and returning the status code """
    
    if (function_name == "add" or function_name == "subtract" or function_name == "multiply"):
        if "x" not in posted_data or "y" not in posted_data:
            return 301  # Missing parameter
        else:
            return 200
    elif (function_name == "division"):
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif int(posted_data["y"]) == 0:
            return 302
        else:
            return 200

def main():
    
    data, operation = get_args()

    print(data)

    result = check_posted_data(data, operation)
    
    print(f"The result of the check is {result}")


if __name__ == "__main__":

    main()
    
    

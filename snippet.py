def check_posted_data(postedData, functionName):
    if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301 #Missing parameter
        else:
            return 200
    elif (functionName == "division"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"])==0:
            return 302
        else:
            return 200
          

if __name__ == "__main__":
  
  data = {"x": 23, "y": 76}
  result = check_posted_data(data, "subtract")
  print(f"The sum of {data.get("x")} and {data.get("y")} is {result}")
  

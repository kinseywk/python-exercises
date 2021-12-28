def prompt(text, expect = str):
  print(text)
  while True:
    try:
      response = input()

      if expect is str:
        return response
      elif expect is int:
        return int(response)
      elif expect is float:
        return float(response)
      elif expect is bool:
        match response:
          case "True":
            return True
          case "False":
            return False
          case _:
            raise ValueError
      else:
        raise "Expected unknown type; currently, only str, int, float, and bool are supported"
    except ValueError:
      print(f"Input must be a '{expect}'")

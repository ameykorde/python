# returns the first match NO NEED TO ADD BREAK AS IT RETURNS ONLY ONE

def match_case(value):
    # Using match-case to simulate switch-case behavior
    match value:
        # First case for when the value is "a"
        case "a":
            return "Case A"
        # Second case for when the value is "b"
        case "b":
            return "Case B"
        # Third case for when the value is "c"
        case "c":
            return "Case C"
        # Default case when no match is found
        case _:
            return "Default Case"

# Test the match_case function
if __name__ == "__main__":
    # Testing with various values
    print(match_case("a"))  # Output: Case A
    print(match_case("b"))  # Output: Case B
    print(match_case("c"))  # Output: Case C
    print(match_case("d"))  # Output: Default Case
